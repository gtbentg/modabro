import pyrogram

import logging

# Configure logging

logging.basicConfig(level=logging.INFO)

# Create a Pyrogram client

bot = pyrogram.Client(

    "my_bot",

    api_id="15428219",

    api_hash="0042e5b26181a1e95ca40a7f7c51eaa7",

    bot_token="5507296374:AAFiZjhKFelrMNXXUoJe8EkjHvua5QeV2q0"

)

# Define the handler for incoming messages

@bot.on_message()

async def handle_message(client, message):

    # Check if the message is a file with a caption

    if message.document and message.document.caption:

        # Get the caption of the file

        caption = message.document.caption

        logging.info(f"Received file with caption: {caption}")

        # Check if the specific text is present in the caption

        if "✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz" in caption:

            # Remove the specific text from the caption

            modified_caption = caption.replace("✅ ɢʀᴏᴜᴘ : @CinimaAdholokaam\n✅ ᴄʜᴀɴɴᴇʟ : @Calinkzz", "")

            logging.info(f"Modified caption: {modified_caption}")

            # Update the caption of the file in the channel

            await client.edit_message_text(

                chat_id=message.chat.id,

                message_id=message.message_id,

                text=modified_caption

            )

# Start the bot

bot.run()

