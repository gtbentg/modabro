import pyrogram

bot = pyrogram.Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5507296374:AAFiZjhKFelrMNXXUoJe8EkjHvua5QeV2q0")

@bot.on_message()

async def handler(message):

    # Check if the message is a file with a caption

    if message.document and message.document.caption:

        # Get the caption of the file

        caption = message.document.caption

        # Remove the text "✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam

        # ✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz" from the caption

        caption = caption.replace("✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam

        ✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz", "")

        # Set the new caption for the file

        message.document.caption = caption

        # Send the file back to the sender

        await message.reply_document(message.document)
                                  
print("🙌🏻🙌🏻")
bot.run()                          
