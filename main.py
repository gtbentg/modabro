from pyrogram import Client, filters

# Create a new Pyrogram client

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5507296374:AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register a message handler

@app.on_message(filters.text)

async def make_text_bold(client, message):

    # Get the original text

    text = message.text

    # Format the text by making it bold

    formatted_text = f"<b>{text}</b>"

    # Reply to the message with the formatted text

    await message.reply_text(formatted_text, parse_mode="HTML")

# Start the bot

app.run()
