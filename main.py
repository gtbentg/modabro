from pyrogram import Client, filters

from pyrogram.types import Message

# Initialize the bot

API_ID = "15428219"
API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"
BOT_TOKEN = "5507296374:AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4"

bot = Client("bold_caption_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Format the caption by making all text bold

def format_caption(caption):

    formatted_caption = f"*{caption}*"

    return formatted_caption

# Process photo messages with a caption

@bot.on_message(filters.photo & filters.caption)

async def process_photo(client, message: Message):

    # Get the photo caption

    caption = message.caption

    # Format the caption by making all text bold

    formatted_caption = format_caption(caption)

    # Edit the message caption with the formatted caption

    await message.edit_caption(

        caption=formatted_caption,

        parse_mode="text"

    )

# Run the bot

bot.run()
