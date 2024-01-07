import main
from telegram.ext import Updater, CommandHandler
from telegram import Update

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{main.variants}')


app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()