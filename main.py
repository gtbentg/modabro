from pyrogram import Client, filters

from pyrogram.types import Message

# Initialize the Pyrogram client

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5492441001:AAGONuW8_PIPFewaLt9V0sOZjIhMXjr0LrQ"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the private channels to forward messages from

private_channels = ["-1001822069031", "-1001630728036"]

# Define the public channel to forward messages to

public_channel = "-1001861161044"

# Define a filter to only forward messages with media (photos, videos, documents, etc.)

media_filter = filters.private & (filters.photo | filters.video | filters.document)

# Define a function to forward the message to the public channel

async def forward_to_public_channel(client: Client, message: Message):

    # Get the chat ID of the public channel

    public_chat = await client.get_chat(public_channel)

    public_chat_id = public_chat.id

    

    # Forward the message to the public channel

    await message.forward(public_chat_id)

# Add a handler for messages in the private channels

@app.on_message(filters.chat(private_channels) & media_filter)

async def handle_private_message(client: Client, message: Message):

    # Forward the message to the public channel

    await forward_to_public_channel(client, message)

# Start the bot

print("readyyyy")

app.run()
