import pyrogram

api_id = "15428219"

api_hash = "0042e5b26181a1e95ca40a7f7c51eaa7"

bot_token = "5507296374:AAFiZjhKFelrMNXXUoJe8EkjHvua5QeV2q0"

client = pyrogram.Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@client.on_message()

async def handle_message(client, message):

    if message.document is not None:

        caption = message.caption

        if "@CinimaAdholokaam" in caption or "@Calinkzz" in caption:

            new_caption = caption.replace("@CinimaAdholokaam", "@MovieBossTG").replace("@Calinkzz", "@MovieBossTG")

            await message.edit(text=f"**{new_caption}**")

client.run()

