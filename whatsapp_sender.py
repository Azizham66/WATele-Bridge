import requests as req
from media_handler import handler

async def send_message(client, msg, jid):
    message_object = await handler(client, msg, jid)
    req.post("http://localhost:3000/send-message", json=message_object)