import pyrogram

import requests

from bs4 import BeautifulSoup

API_KEY = "k_ouua140i"

def get_new_releases():

    response = requests.get(

        "https://imdb-api.com/en/API/TopRatedTV/" + API_KEY

    )

    soup = BeautifulSoup(response.text, "html.parser")

    new_releases = []

    for movie in soup.find_all("div", class_="lister-item mode-advanced"):

        title = movie.find("h3").text

        release_date = movie.find("span", class_="lister-item-year").text

        new_releases.append((title, release_date))

    return new_releases

bot = pyrogram.Client("my_bot", api_id=15428219, api_hash="0042e5b26181a1e95ca40a7f7c51eaa7")

@bot.on_message()

async def handle_message(message):

    if message.text == "/start":

        await message.reply(

            "Welcome to the new movie and series release bot! I will send you a list of new releases every day."

        )

        new_releases = get_new_releases()

        for title, release_date in new_releases:

            await message.reply(f"New release: {title} ({release_date})")

bot.run()
