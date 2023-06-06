from pyrogram import Client, filters

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5492441001:AAGONuW8_PIPFewaLt9V0sOZjIhMXjr0LrQ"

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# replace with your own channel IDs

channel_ids = [-1001630728036, -1001822069031]

# replace with your own destination channel ID

destination_channel_id = -1001861161044

# create a function to forward messages

@app.on_message(filters.chat(channel_ids))

def forward_to_destination(client, message):

    client.forward_messages(destination_channel_id, message.chat.id, message.message_id)

# run the app

print("hyyyy")

app.run()
