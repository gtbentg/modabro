import pyrogram

import requests

import time

API_KEY = "k_ouua140i"

def get_new_releases():

    response = requests.get(

        "https://imdb-api.com/en/API/TopRatedTV/" + API_KEY

    )
    
    print(response.content)  # Print the response content
    
    data = response.json()

    new_releases = []

    for item in data['items']:

        title = item['title']

        release_date = item['year']

        new_releases.append((title, release_date))

    return new_releases

bot = pyrogram.Client("my_bot", api_id=15428219, api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5310839293:AAE2IQxhx9kwVwbhxk9MBu85GM7-gHoSqGI")

@bot.on_message()

async def handle_message(client, message):

    if message.text == "/start":

        await message.reply_text(

            "Welcome to the new movie and series release bot! I will send you a list of new releases every day."

        )

async def send_new_releases():

    new_releases = get_new_releases()

    for title, release_date in new_releases:

        await bot.send_message(chat_id="YOUR_CHAT_ID", text=f"New release: {title} ({release_date})")

    while True:

        time.sleep(86400)  # Wait for 24 hours

        new_releases = get_new_releases()

        for title, release_date in new_releases:

            await bot.send_message(chat_id="YOUR_CHAT_ID", text=f"New release: {title} ({release_date})")

print("okkk")

bot.run(send_new_releases())

