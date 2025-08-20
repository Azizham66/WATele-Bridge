# 📱 Telegram-to-WhatsApp Bridge 🚀

Forward messages (text, images, audio, and video) from a Telegram chat to a WhatsApp number automatically using a self-hosted WhatsApp API.

It leverages:

- [Telethon](https://docs.telethon.dev/) 🛠️ for interacting with Telegram.
- A self-hosted WhatsApp API (like [Baileys-API](https://github.com/Azizham66/Baileys-API)) 💬 for sending WhatsApp messages.

---

## ✨ Features

- Forward Telegram messages to WhatsApp in real-time ⏱️.
- Supports text, images 🖼️, audio 🎵, and video 🎥 messages.
- Handles media downloads automatically 💾.
- Fully self-hosted, no third-party cloud services required 🏠.

---

## 📝 Requirements

- Python 3.9 or higher 🐍
- Node.js and the self-hosted WhatsApp API running locally on port `3000`
- Telegram API credentials (`api_id` and `api_hash`)
- Your target Telegram chat ID and WhatsApp JID

---

## 🚀 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/Azizham66/WATele-Bridge.git
cd WATele-Bridge
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure your credentials:**

- Copy `config/config_example.py` to `config/config.py`:

```bash
cp config/config_example.py config/config.py
```

- Fill in your Telegram API credentials, chat ID, WhatsApp JID, and optional media path in `config/config.py`.

### How to get Telegram `api_id` and `api_hash` 🔑:

1. Go to [my.telegram.org](https://my.telegram.org).
2. Log in with your Telegram account.
3. Click on "API development tools".
4. Create a new application to get `api_id` and `api_hash`.

### How to get Telegram chat ID 🆔:

- Use a bot like [@userinfobot](https://t.me/useridbot) in the chat you want to monitor, or run a Telethon script to fetch it.

### How to get WhatsApp JID 📩:

- Individual chat: `123456789@s.whatsapp.net`
- Group chat: `123456789-123456@g.us`
- Or fetch it via the `/groups` endpoint of your self-hosted WhatsApp API.

Example `config_example.py`:

```python
# Your Telegram API ID
api_id = ""
# Your Telegram API hash
api_hash = ""
# The username or ID of the Telegram chat/group/channel you want to listen from
telegram_chat = ""
# The WhatsApp chat/group ID you want to send the message to. ex: 123456789@s.whatsapp.net
jid = ""
# Path to store downloaded media temporarily
media_path = ""
```

4. **Start the WhatsApp API** 💻:

You can self-host my pre-built API from [Baileys-API](https://github.com/Azizham66/Baileys-API)

```bash
cd path/to/WATele-Bridge
node index.js
```

Make sure to replace `localhost:3000` with your corresponding server URL in `whatsapp_sender.py` 🌐.

---

## 🏃‍♂️ Usage

Run the Telegram-to-WhatsApp bridge:

```bash
python main.py
```

Any new message in your configured Telegram chat will be forwarded to the specified WhatsApp number automatically ✅.

---

## 📦 Supported Message Types

- Text
- Images 🖼️
- Audio 🎵
- Videos 🎥

Unsupported media types will be sent as a placeholder text indicating an unsupported format ❌.

---

## 🗂 Project Structure

```
├── main.py             # Entry point for the Telegram listener
├── media_handler.py    # Handles downloading media from Telegram
├── whatsapp_sender.py  # Sends messages to WhatsApp via the API
└── config
    ├── config.py       # Configuration for API credentials and paths
    └── config_example.py  # Template for creating your own config.py
```

---

## 📝 Notes

- Ensure your WhatsApp API is running and connected before running this script ✅.
- Media files are downloaded to the `media_path` folder temporarily before sending 💾.

---

## ⚖️ License

MIT License

