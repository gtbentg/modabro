import pyrogram

import requests

import time

# Function to fetch movie details using OMDB API

def get_movie_details(title):

    params = {

        "apikey": "96b11f45",

        "t": title,

        "type": "movie"

    }

    response = requests.get("http://www.omdbapi.com/", params=params)

    data = response.json()

    return data

# Function to fetch movie poster using Unsplash API

def get_movie_poster(movie_title):

    headers = {

        "Authorization": "Bearer 64Q3Al1bHpRg_QqTeyC2L0Ti6WOQk3ZiKpgjwO72JJ4"

    }

    params = {

        "query": movie_title,

        "orientation": "portrait",

        "per_page": 1

    }

    response = requests.get("https://api.unsplash.com/search/photos", headers=headers, params=params)

    data = response.json()

    if "results" in data and len(data["results"]) > 0:

        return data["results"][0]["urls"]["regular"]

    else:

        return None

# Function to get new movie releases

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

# Pyrogram bot client

bot = pyrogram.Client("my_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOU_TOKEN")

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

        if movie_details and "Poster" in movie_details:

            movie_poster = get_movie_poster(title)

            caption = f"New release: {title} ({release_date})\n\n{movie_details['Plot']}"

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

            if movie_details and "Poster" in movie_details:

                movie_poster = get_movie_poster(title)

                caption = f"New release: {title} ({release_date})\n\n{movie_details['Plot']}"

                if movie_poster:

                    await bot.send_photo(chat_id="@GT_ben", photo=movie_poster, caption=caption)

                else:

                    await bot.send_message(chat_id="@GT_ben", text=caption)

            else:

                await bot.send_message(chat_id="@GT_ben", text=f"New release: {title} ({release_date})")

bot.run(send_new_releases())

