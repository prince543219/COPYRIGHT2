import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from motor.motor_asyncio import AsyncIOMotorClient

# CONFIG
API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
OWNER_ID = 123456789

MONGO_URI = "mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "nsfw_bot"

app = Client("nsfw_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# MONGODB
mongo = AsyncIOMotorClient(MONGO_URI)
db = mongo[DB_NAME]

users_col = db.users
chats_col = db.chats
warns_col = db.warns


# LOAD FILTER WORDS
def load_words():
    with open("nsfw.txt", "r") as f:
        return [x.strip().lower() for x in f.readlines()]

NSFW_WORDS = load_words()


# SAVE USERS
@app.on_message(filters.private)
async def save_user(_, message):
    if not await users_col.find_one({"_id": message.from_user.id}):
        await users_col.insert_one({"_id": message.from_user.id})


# SAVE CHATS
@app.on_message(filters.group)
async def save_chat(_, message):
    if not await chats_col.find_one({"_id": message.chat.id}):
        await chats_col.insert_one({"_id": message.chat.id})


# WARNING SYSTEM
async def add_warn(user, chat):
    data = await warns_col.find_one({"user": user, "chat": chat})
    
    if data:
        count = data["count"] + 1
        await warns_col.update_one({"user": user, "chat": chat}, {"$set": {"count": count}})
    else:
        count = 1
        await warns_col.insert_one({"user": user, "chat": chat, "count": count})
    
    return count


# FILTER
@app.on_message(filters.group & filters.text)
async def filter_msg(client, message):

    if message.from_user.id == OWNER_ID:
        return

    text = message.text.lower()

    if any(word in text for word in NSFW_WORDS):

        await message.delete()

        count = await add_warn(message.from_user.id, message.chat.id)

        username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name

        if count == 1:
            txt = f"""⚠️ WARNING #1 - FIRST STRIKE

{username}

Your message was deleted.

🚫 Reason: Restricted content

📊 Warning: 1/3
⏭️ Next: 2nd strike = mute"""
        
        elif count == 2:
            txt = f"""⚠️ WARNING #2

{username}

📊 Warning: 2/3
⏭️ Next: Mute"""
        
        else:
            try:
                await client.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    permissions={"can_send_messages": False},
                    until_date=60
                )
                txt = f"🔇 {username} muted (3rd strike)"
            except:
                txt = f"{username} - bot needs admin rights"

        await message.reply(txt)


# BROADCAST
async def send_msg(chat_id, message):
    try:
        await message.copy(chat_id)
        return True
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(chat_id, message)
    except:
        return False


@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message):

    if not message.reply_to_message:
        return await message.reply("Reply to message")

    status = await message.reply("Broadcasting...")

    users = [u["_id"] async for u in users_col.find()]
    chats = [c["_id"] async for c in chats_col.find()]

    done = fail = 0

    for i in users + chats:
        if await send_msg(i, message.reply_to_message):
            done += 1
        else:
            fail += 1

    await status.edit(f"✅ Done\n✔ {done}\n❌ {fail}")


# STATS
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(_, message):

    users = await users_col.count_documents({})
    chats = await chats_col.count_documents({})

    await message.reply(
        f"""📊 Stats

👤 Users: {users}
👥 Chats: {chats}
📦 Total: {users + chats}
"""
    )


app.run()
