from pyrogram import Client, filters

from pyrogram.types import InputMediaPhoto

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5507296374:AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4"

app = Client("my_bot_token", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.photo)

def bold_caption(client, message):

    # Get the caption of the photo

    caption = message.caption

    # Check if the caption is not empty

    if caption:

        # Add bold formatting to the caption text

        bold_caption = f"<b>{caption}</b>"

        # Replace the original caption with the bold caption

        message.caption = bold_caption

        # Send the photo with the updated caption

        client.send_photo(chat_id=message.chat.id, photo=message.photo.file_id, caption=bold_caption)

print("okkk")

app.run()
