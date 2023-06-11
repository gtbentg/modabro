from pyrogram import Client, filters

import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_ID = '15428219'
API_HASH = '0042e5b26181a1e95ca40a7f7c51eaa7'
BOT_TOKEN = '5310839293:AAE2IQxhx9kwVwbhxk9MBu85GM7-gHoSqGI'

# Replace 'YOUR_IMDB_API_KEY' with your actual IMDb API key

imdb_api_key = 'k_aaaaaaaa'

# Create the Pyrogram client

app = Client("imdb_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define a function to send a message with a photo

def send_photo(bot, chat_id, photo_url, caption):

    bot.send_photo(chat_id=chat_id, photo=photo_url, caption=caption)

# Define a function to check for new movie and series releases

def check_for_updates():

    # Make a request to the IMDb API to get the latest movie and series releases

    url = f'https://imdb-api.com/en/API/ComingSoon/{imdb_api_key}'

    response = requests.get(url)

    data = response.json()

    # Iterate over the movies and series

    for item in data['items']:

        # Check if the item is a movie or series

        if item['titleType'] in ['movie', 'tvSeries']:

            title = item['title']

            image_url = item['image']

            description = item['description']

            # Replace 'YOUR_CHAT_ID' with the chat ID of the recipient

            chat_id = 'YOUR_CHAT_ID'

            # Send the message with the photo

            send_photo(app, chat_id, image_url, f'{title}\n\n{description}')

# Define a handler for the /start command

@app.on_message(filters.command('start'))

def start_command(client, message):

    message.reply_text('Bot started!')

# Define a handler for the /check_updates command

@app.on_message(filters.command('check_updates'))

def check_updates_command(client, message):

    check_for_updates()

# Start the bot

app.run()

