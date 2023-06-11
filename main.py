import pyrogram

import requests

import time

def get_new_releases():

    response = requests.get("http://www.omdbapi.com/?s=new&type=movie&apikey=96b11f45")

    try:

        data = response.json()

        if data['Response'] == 'True':

            new_releases = []

            for item in data['Search']:

                title = item['Title']

                release_date = item['Year']

                new_releases.append((title, release_date))

            return new_releases

        else:

            print("Error retrieving new releases from the API:")

            print(data['Error'])

            return []

    except ValueError:

        print("Error decoding response as JSON:")

        print(response.content)

        return []

bot = pyrogram.Client("my_bot", api_id=15428219, api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5310839293:AAFf3gugWXvL3_vBpumyxcaC0VovBZ-TbuY")

@bot.on_message()

async def handle_message(client, message):

    if message.text == "/start":

        await message.reply_text(

            "Welcome to the new movie release bot! I will send you a list of new releases every day."

        )

async def send_new_releases():

    await bot.start()  # Start the Pyrogram client

    new_releases = get_new_releases()

    for title, release_date in new_releases:

        await bot.send_message(chat_id="1653535224", text=f"New release: {title} ({release_date})")

    while True:

        time.sleep(86400)  # Wait for 24 hours

        new_releases = get_new_releases()

        for title, release_date in new_releases:

            await bot.send_message(chat_id="1653535224", text=f"New release: {title} ({release_date})")

bot.run(send_new_releases())

