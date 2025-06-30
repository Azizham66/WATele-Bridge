from config.config import api_id,api_hash,telegram_chat,jid
from telethon import TelegramClient, events
import asyncio
from whatsapp_sender import send_message

client = TelegramClient("Test Session", api_id, api_hash)

@client.on(events.NewMessage(chats = telegram_chat))
async def on_message(event):
    msg = event.message
    try:
        await send_message(client, msg, jid)
        print(msg.message)
    except Exception as e:
        print(e)


client.start()
client.run_until_disconnected()