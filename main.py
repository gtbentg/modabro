from pyrogram import Client, filters

# Initialize the Pyrogram client

API_ID = '15428219'

API_HASH = '0042e5b26181a1e95ca40a7f7c51eaa7'

BOT_TOKEN = '5507296374:AAFiZjhKFelrMNXXUoJe8EkjHvua5QeV2q0'

app = Client('file_caption_editor_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)

def process_file_caption(client, message):

    # Check if the message is from a channel

    if message.chat.type == 'channel':

        caption = message.caption

        if caption is not None:

            # Check if the specific text is present in the caption

            if "=========== • ✠ • ===========\n✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz\n=========== • ✠ • ===========" in caption:

                # Remove the specific text from the caption

                updated_caption = caption.replace("=========== • ✠ • ===========\n✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz\n=========== • ✠ • ===========", "")

                # Edit the message caption

                client.edit_message_caption(

                    chat_id=message.chat.id,

                    message_id=message.message_id,

                    caption=updated_caption

                )

# Run the client
print("❗️❗️")
app.run()

