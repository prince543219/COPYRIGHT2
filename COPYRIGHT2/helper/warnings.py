"""Warning system for copyright violations"""
from pymongo import MongoClient
from config import MONGO_URL
from datetime import datetime

client = MongoClient(MONGO_URL)
warnings_db = client["COPYRIGHT2"]["warnings"]

async def get_warnings(user_id, chat_id):
    """Get warning count for user in specific chat"""
    data = warnings_db.find_one({"user_id": user_id, "chat_id": chat_id})
    return data["warnings"] if data else 0

async def add_warning(user_id, chat_id):
    """Add warning to user"""
    data = warnings_db.find_one({"user_id": user_id, "chat_id": chat_id})
    if data:
        new_count = data["warnings"] + 1
        warnings_db.update_one(
            {"user_id": user_id, "chat_id": chat_id},
            {"$set": {"warnings": new_count, "last_warn": datetime.now()}}
        )
    else:
        new_count = 1
        warnings_db.insert_one({
            "user_id": user_id,
            "chat_id": chat_id,
            "warnings": new_count,
            "last_warn": datetime.now()
        })
    return new_count

async def reset_warnings(user_id, chat_id):
    """Reset warnings for user"""
    warnings_db.delete_one({"user_id": user_id, "chat_id": chat_id})
