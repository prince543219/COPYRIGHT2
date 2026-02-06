# 🛡️ COPYRIGHT2 - Advanced Copyright Protection Bot

[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://t.me/COPYRIGHTXTBOT)
[![GitHub](https://img.shields.io/badge/GitHub-DAXXTEAM-green)](https://github.com/DAXXTEAM/COPYRIGHT2)

Professional Telegram bot for protecting groups from copyright violations and illegal content.

## 🌟 Features

### 🔒 Advanced Protection
- **100+ Forbidden Keywords** covering all violation categories
- **Smart Detection** - Case-insensitive & obfuscation-resistant
- **Card Number Protection** - Auto-detects credit card patterns
- **Progressive Warning System** - 3 strikes before mute
- **Admin Bypass** - Group owners and admins are not restricted

### ⚖️ Warning System

| Strike | Action | Duration |
|--------|--------|----------|
| 1st | Warning Only | - |
| 2nd | Warning + Alert | - |
| 3rd | **Mute** | 1 minute |
| 4th | **Mute** | 2 minutes |
| 5th | **Mute** | 3 minutes |
| 6+ | **Progressive Mute** | Increases each time |

### 🚫 Protected Categories

**Entertainment Piracy:**
- Movies & TV Shows (Bollywood, Hollywood, OTT)
- Music & Albums
- Games & Software

**Educational Content:**
- Books & PDFs (NCERT, Textbooks)
- Paid Courses (Udemy, Coursera)

**Premium Services:**
- Streaming Accounts (Netflix, Spotify, etc.)
- Cracked/Modded Apps

**Illegal Activities:**
- Carding & Fraud Keywords
- Hacking Tools
- Spam Bots

## 🚀 Deployment

### Requirements
- Python 3.10+
- MongoDB Database
- Telegram Bot Token

### Quick Start

1. **Clone Repository**
```bash
git clone https://github.com/DAXXTEAM/COPYRIGHT2.git
cd COPYRIGHT2
```

2. **Install Dependencies**
```bash
pip3 install -r requirements.txt
```

3. **Configure Bot**
Edit `config.py`:
```python
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
OWNER_ID = YOUR_TELEGRAM_ID
MONGO_URL = "YOUR_MONGODB_URL"
```

4. **Run Bot**
```bash
python3 -m COPYRIGHT2
```

### Deploy on VPS
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run in background
nohup python3 -m COPYRIGHT2 > bot.log 2>&1 &
```

## 📋 Commands

- `/start` - Bot introduction
- `/ping` - Check bot status
- `/broadcast` - Send message to all users (Owner only)
- `/announce` - Send to all groups (Owner only)

## 🛠️ Configuration

### Add Custom Keywords
Edit `COPYRIGHT2/modules/main.py`:
```python
FORBIDDEN_KEYWORDS = [
    "your_keyword_1",
    "your_keyword_2",
    # Add more...
]
```

### Adjust Mute Durations
Modify strike actions in the message handler function.

## 🤝 How It Works

1. **Detection**: Bot monitors all messages for forbidden content
2. **Bypass**: Admins and owners are automatically exempted
3. **Delete**: Violating messages are instantly removed
4. **Warn**: User receives detailed warning with strike count
5. **Mute**: After 3 warnings, progressive mute system activates
6. **Track**: MongoDB tracks warnings per user per group

## 🔐 Security Features

- **Obfuscation Detection**: Catches "p o r n", "p@rn", etc.
- **Case-Insensitive**: Works with CAPS, lowercase, MiXeD
- **Pattern Matching**: Detects credit card numbers
- **Smart Cleaning**: Removes special characters for analysis

## 📊 Statistics

- **100+ Protected Keywords**
- **6+ Content Categories**
- **Progressive Punishment System**
- **MongoDB-Backed Tracking**

## 🌐 Support & Links

- **Support Group**: [Join Here](https://t.me/+sG0Q1eYuricyNWE1)
- **Bot**: [@COPYRIGHTXTBOT](https://t.me/COPYRIGHTXTBOT)
- **GitHub**: [DAXXTEAM](https://github.com/DAXXTEAM)

## 📜 License

This project is licensed under MIT License.

## ⚠️ Disclaimer

This bot is for educational purposes and group moderation. Users are responsible for compliance with local laws and Telegram's Terms of Service.

## 👨‍💻 Developer

**DAXX** - [@iam_daxx](https://t.me/iam_daxx)

---

Made with ❤️ by DAXXTEAM
