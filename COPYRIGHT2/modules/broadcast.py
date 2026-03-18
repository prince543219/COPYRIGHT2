import asyncio
import traceback
from config import OWNER_ID
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from COPYRIGHT2 import COPYRIGHT2 as app
from COPYRIGHT2.helper import get_users, get_chats


# ✅ Safe send function
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None

    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(user_id, message)

    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated"

    except UserIsBlocked:
        return 400, f"{user_id} : blocked"

    except PeerIdInvalid:
        return 400, f"{user_id} : invalid"

    except Exception:
        return 500, traceback.format_exc()


# ✅ BROADCAST (copy message)
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message):

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast.")

    status = await message.reply_text("Broadcast started...")

    users = await get_users() or []
    chats = await get_chats() or []

    done_users = failed_users = 0
    done_chats = failed_chats = 0

    # USERS
    for user in users:
        code, _ = await send_msg(user, message.reply_to_message)
        if code == 200:
            done_users += 1
        else:
            failed_users += 1
        await asyncio.sleep(0.1)

    # GROUPS
    for chat in chats:
        code, _ = await send_msg(chat, message.reply_to_message)
        if code == 200:
            done_chats += 1
        else:
            failed_chats += 1
        await asyncio.sleep(0.1)

    await status.edit_text(
        f"""✅ **Broadcast Completed**

👤 Users: {done_users} success | {failed_users} failed  
👥 Chats: {done_chats} success | {failed_chats} failed
"""
    )


# ✅ ANNOUNCE (forward message)
@app.on_message(filters.command("announce") & filters.user(OWNER_ID))
async def announce(client, message):

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to announce.")

    status = await message.reply_text("Announce started...")

    users = await get_users() or []
    chats = await get_chats() or []

    failed_users = 0
    failed_chats = 0

    # USERS
    for user in users:
        try:
            await message.reply_to_message.forward(user)
            await asyncio.sleep(0.1)
        except Exception:
            failed_users += 1

    # CHATS
    for chat in chats:
        try:
            await message.reply_to_message.forward(chat)
            await asyncio.sleep(0.1)
        except Exception:
            failed_chats += 1

    await status.edit_text(
        f"""✅ **Announce Completed**

👤 Failed Users: {failed_users}
👥 Failed Chats: {failed_chats}
"""
    )


# ✅ STATS COMMAND
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(_, message):

    users = await get_users() or []
    chats = await get_chats() or []

    total_users = len(users)
    total_chats = len(chats)

    await message.reply_text(
        f"""📊 **Bot Stats**

👤 Total Users: {total_users}
👥 Total Chats: {total_chats}
📦 Total Reach: {total_users + total_chats}
"""
    )
