from pyrogram import Client, filters
from pyrogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_edited_message(filters.group & ~filters.me)
async def debug_edited(client, edited_message: Message):
    """Debug to see what Telegram sends"""
    logger.info(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    EDITED MESSAGE EVENT:
    Message ID: {edited_message.id}
    Edit Date: {edited_message.edit_date}
    Text: {edited_message.text}
    Caption: {edited_message.caption}
    Reactions: {edited_message.reactions if hasattr(edited_message, 'reactions') else 'N/A'}
    Media: {edited_message.media if hasattr(edited_message, 'media') else 'N/A'}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)
