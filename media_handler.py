from telethon.tl.types import (
    MessageMediaPhoto,
    MessageMediaDocument,
    DocumentAttributeAudio,
    DocumentAttributeVideo
)

from config.config import media_path

async def handler(client, msg, jid):
    if msg.media:
        if isinstance(msg.media, MessageMediaPhoto):
            path = await client.download_media(msg, media_path) # replace with your respective path
            return {
                "jid": jid,
                "message": {
                    "image": {
                        "url": path
                    },
                    "caption": msg.message or ""
                }
            }
        elif isinstance(msg.media, MessageMediaDocument):
            doc = msg.document

            if any(isinstance(attr, DocumentAttributeAudio) for attr in doc.attributes):
                path = await client.download_media(msg, media_path) # replace with your respective path
                return {
                    "jid": jid,
                    "message": {
                        "audio": {
                            "url": path
                        },
                        "mimetype": "audio/mp4"
                    }
                }

            elif any(isinstance(attr, DocumentAttributeVideo) for attr in doc.attributes):
                path = await client.download_media(msg, media_path)
                return {
                    "jid": jid,
                    "message": {
                        "video": {
                            "url": path
                        },
                        "caption": msg.message or "",
                        "pvt": False
                    }
                }
            else:
                return {
                    "jid": jid,
                    "message": {
                        "text": "Unsupported Document Format"
                    }
                }
        else:
            return {
                "jid": jid,
                "message": {
                    "text": "Unsupported Media Format"
                }
            }

    elif msg.message:
        return {
            "jid": jid,
            "message": {
                "text": msg.message
            }
        }
    else:
        return {
            "jid": jid,
            "message": {
                "text": "Received a message with an unsupported content"
            }
        }