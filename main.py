from pyrogram import Client, filters

# Create a new Telegram bot using the API token

bot = Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5507296374:AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4")

@bot.on_message(filters.document)

def delete_documents(bot, message):

    caption = message.caption

    if caption:

        updated_caption = caption.replace("=========== • ✠ • ===========\n✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz\n=========== • ✠ • ===========", "")

        if updated_caption != caption:

            bot.edit_message_caption(chat_id=message.chat.id, message_id=message.message_id, caption=updated_caption)

# Run the bot
print("ok💝")
bot.run()

