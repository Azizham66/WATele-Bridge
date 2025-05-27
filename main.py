from config.config import api_id,api_hash,telegram_chat
from telethon import TelegramClient, events
import asyncio

client = TelegramClient("Test Session", api_id, api_hash)

@client.on(events.NewMessage(chats = telegram_chat))
async def on_message(event):
    msg = event.message

    if msg.media:
        print("Message contains media")
        path = await client.download_media(msg, './downloads/')
        print(f"Saved to: {path}")

        if msg.message:
            print(f"with the caption: {msg.message}")
    elif msg.message:
        print(msg.message)
    else:
        print("Received a message with unsupported content")



client.start()
client.run_until_disconnected()