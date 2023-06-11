from pyrogram import Client

import requests

# Enter your API ID, API hash, and bot token here

API_ID = '15428219'

API_HASH = '0042e5b26181a1e95ca40a7f7c51eaa7'

BOT_TOKEN = '5310839293:AAE2IQxhx9kwVwbhxk9MBu85GM7-gHoSqGI'

# Create the client

client = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the function to send updates

def send_updates():

    # Make a request to the website

    response = requests.get('https://imdb-api.com/en/API/ComingSoon/k_ouua140i')

    # Get the JSON data from the response

    data = response.json()

    # Send the updates

    for item in data['items']:

        if item['type'] == 'movie':

            # Get the movie title and image URL

            title = item['title']

            image_url = item['image']

            # Download the image

            response = requests.get(image_url)

            image_data = response.content

            # Send the message with the photo

            client.send_photo(chat_id='@my_channel', photo=image_data, caption=title)

        elif item['type'] == 'tvSeries':

            # Get the series title and image URL

            title = item['title']

            image_url = item['image']

            # Download the image

            response = requests.get(image_url)

            image_data = response.content

            # Send the message with the photo

            client.send_photo(chat_id='@my_channel', photo=image_data, caption=title)

    
# Run the client and send updates every hour

with client:

    client.loop.run_until_complete(send_updates())

    client.run()
