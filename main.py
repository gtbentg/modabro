from pyrogram import Client, filters

# Your API credentials

API_ID = '15428219''

API_HASH = '0042e5b26181a1e95ca40a7f7c51eaa7'

BOT_TOKEN = '5492441001:AAGONuW8_PIPFewaLt9V0sOZjIhMXjr0LrQ'

# The private channel where the bot will monitor for messages

private_channel = '-1001649665241'

# The target channel where the bot will forward the files

target_channel = '-1001646628986'

# Create the Pyrogram client

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Filter to check if the message contains a channel link

channel_link_filter = filters.regex(r"(?:https?://)?(?:www\.)?(?:t\.me/|telegram\.me/|@)?(\w+)")

# Filter to check if the message has a new file

file_filter = filters.document | filters.video | filters.audio

@app.on_message(filters.chat(private_channel) & filters.text & channel_link_filter)

async def handle_channel_link(client, message):

    # Extract the channel username from the link

    match = channel_link_filter.match(message.text)

    if match:

        channel_username = match.group(1)

        # Join the channel to get access to its messages

        try:

            channel_info = await app.get_chat(channel_username)

            await app.join_chat(channel_info.id)

        except Exception as e:

            print(f"Error joining channel {channel_username}: {str(e)}")

    

@app.on_message(filters.chat(private_channel) & file_filter)

async def handle_new_file(client, message):

    # Forward the new file to the target channel

    try:

        await app.copy_message(chat_id=target_channel, from_chat_id=message.chat.id, message_id=message.message_id)

    except Exception as e:

        print(f"Error forwarding file to {target_channel}: {str(e)}")

# Start the bot

print("startedddyyyy")

app.run()

