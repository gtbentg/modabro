from telegram import Bot, Update, ParseMode

from telegram.ext import Updater, MessageHandler, Filters

# Initialize the bot

bot = Bot(token="5507296374:AAHzdrj_nru8XQbNtRSAraVQ3eJd6r3HIC4")

# Process messages with a photo and caption

def process_message(update: Update, context):

    message = update.effective_message

    if message.photo and message.caption:

        caption = message.caption

        # Format the caption by making all text bold

        formatted_caption = f"<b>{caption}</b>"

        # Reply to the message with the formatted caption

        message.reply_photo(

            photo=message.photo[-1].file_id,

            caption=formatted_caption,

            parse_mode=ParseMode.HTML

        )

# Set up the Telegram bot

updater = Updater(bot=bot, use_context=True)

dispatcher = updater.dispatcher

# Register the message handler

dispatcher.add_handler(MessageHandler(Filters.photo & Filters.caption, process_message))

# Start the bot

updater.start_polling()

updater.idle()

