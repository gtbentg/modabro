import pyrogram

# Get your API ID and hash from https://core.telegram.org/api/obtaining_api_id

api_id = "15428219"

api_hash = "0042e5b26181a1e95ca40a7f7c51eaa7"

bot_token = "5507296374:AAFiZjhKFelrMNXXUoJe8EkjHvua5QeV2q0"

# Create a Pyrogram client

client = pyrogram.Client(

    "my_bot",

    api_id=api_id,

    api_hash=api_hash,

    

    bot_token=bot_token

)

# Define a function that replaces the text "@CinimaAdholokaam" and "@Calinkzz" with "@MovieBossTG" in a caption

def replace_text(caption):

    caption = caption.replace("@CinimaAdholokaam", "@MovieBossTG")

    caption = caption.replace("@Calinkzz", "@MovieBossTG")

    return caption

# Listen for messages

@client.on_message()

async def handle_message(client, message):

    # Check if the message is a file with a caption

    if message.document and message.caption:

        # Replace the text "@CinimaAdholokaam" and "@Calinkzz" with "@MovieBossTG" in the caption

        caption = replace_text(message.caption)

        # Send the new caption along with the file

        await message.reply_document(message.document, caption=caption)

# Run the bot

print("🙌🏻💝💝🙌🏻")

client.run()

