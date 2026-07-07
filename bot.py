from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات مدیریت گروه فعال شد ✅")

async def filter_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    bad_words = ["فحش1", "فحش2"]

    for word in bad_words:
        if word in text:
            await update.message.delete()
            await update.message.chat.send_message(
                "⚠️ لطفاً قوانین گروه را رعایت کنید."
            )
            break

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_words))

print("Bot is running...")
app.run_polling()
