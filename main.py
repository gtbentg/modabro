from pyrogram import Client, filters

# Create a new Telegram bot using the API token

bot = Client("my_bot", api_id=YOUR_API_ID, api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_TOKEN")

@bot.on_message(filters.document)

def delete_documents(bot, message):

    caption = message.caption

    if caption:

        updated_caption = caption.replace("=========== • ✠ • ===========\n✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz\n=========== • ✠ • ===========", "")

        if updated_caption != caption:

            bot.edit_message_caption(chat_id=message.chat.id, message_id=message.message_id, caption=updated_caption)

# Run the bot

bot.run()

