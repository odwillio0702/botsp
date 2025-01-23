from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7534968024:AAGzt6dSrfXJvDKBahWku5ZYsYd9HNhM-XA'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('ы')


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()