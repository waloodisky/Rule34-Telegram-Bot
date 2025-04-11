BotToken="Replace with your bot token"
Preference=""
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from rule34Py import rule34Py
def rule34(update: Update, context: CallbackContext) -> None:
    tag = Preference if not context.args else context.args[0]
    random = rule34Py().random_post([tag])
    image_url = random.image
    update.message.reply_photo(photo=image_url)
def main():
    updater = Updater(BotToken, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('rule34', rule34))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
