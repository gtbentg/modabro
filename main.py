from pyrogram import Client, filters

from pyrogram.types import Message

# Initialize the bot

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5507296374:AAG6NrqWdRGwVqPmMPDJLMvuieXUsJlI8p8"

bot = Client("caption_formatting_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Format the caption by making all text bold

def format_caption(caption):

    bold_caption = f"<b>{caption}</b>"

    return bold_caption

# Process messages with a photo and caption

@bot.on_message(filters.photo & filters.caption)

async def process_message(client, message: Message):

    # Get the photo caption

    caption = message.caption

    # Format the caption by making all text bold

    formatted_caption = format_caption(caption)

    # Reply to the message with the formatted caption

    await message.reply_photo(

        photo=message.photo.file_id,

        caption=formatted_caption,

        parse_mode="HTML"

    )

# Run the bot

print("okk sett")

bot.run()

