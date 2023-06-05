AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4"

bot = Client("bold_caption_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Format the caption by making all text bold

def format_caption(caption):

    formatted_caption = f"*{caption}*"

    return formatted_caption

# Process photo messages with a caption

@bot.on_message(filters.photo & filters.caption)

