import pyrogram

import requests

import time

# Function to fetch movie details using IMDb API

def get_movie_details(title):

    response = requests.get(f"https://imdb-api.com/en/API/SearchMovie/96b11f45/{title}")

    data = response.json()

    return data

# Function to fetch movie poster using IMDb API

def get_movie_poster(imdb_id):

    response = requests.get(f"https://imdb-api.com/en/API/Posters/96b11f45/{imdb_id}")

    data = response.json()

    if "items" in data and len(data["items"]) > 0:

        return data["items"][0]["image"]

    else:

        return None

# Function to get new movie releases

def get_new_releases():

    response = requests.get("https://imdb-api.com/en/API/ComingSoonMovies/96b11f45")

    try:

        data = response.json()

        if data['errorMessage'] == '':

            new_releases = []

            for item in data['items']:

                title = item['title']

                release_date = item['releaseState']

                new_releases.append((title, release_date))

            return new_releases

        else:

            print("Error retrieving new releases from the API:")

            print(data['errorMessage'])

            return []

    except ValueError:

        print("Error decoding response as JSON:")

        print(response.content)

        return []

# Pyrogram bot client

bot = pyrogram.Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5310839293:AAET_Mg291vMOAXwKIORIVo5g9bAToruUek")

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

        movie_details = get_movie_details(title)

        if movie_details and "imDb" in movie_details:

            imdb_id = movie_details["imDb"]["id"]

            movie_poster = get_movie_poster(imdb_id)

            caption = f"New release: {title} ({release_date})\n\n{movie_details['plot']}"

            if movie_poster:

                await bot.send_photo(chat_id="@GT_ben", photo=movie_poster, caption=caption)

            else:

                await bot.send_message(chat_id="@GT_ben", text=caption)

        else:

            await bot.send_message(chat_id="@GT_ben", text=f"New release: {title} ({release_date})")

    while True:

        time.sleep(86400)  # Wait for 24 hours

        new_releases = get_new_releases()

        for title, release_date in new_releases:

            movie_details = get_movie_details(title)

            if movie_details and "imDb" in movie_details:

                imdb_id = movie_details["imDb"]["id"]

                movie_poster = get_movie_poster(imdb_id)

                caption = f"New release: {title} ({release_date})\n\n{movie_details['plot']}"

                if movie_poster:

                    await bot.send_photo(chat_id="@GT_ben", photo=movie_poster, caption=caption)

                else:

                    await bot.send_message(chat_id="@GT_ben", text=caption)

            else:

                await bot.send_message(chat_id="@GT_ben", text=f"New release: {title} ({release_date})")

bot.run(send_new_releases())

