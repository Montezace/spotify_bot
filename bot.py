import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from config import TELEGRAM_BOT_TOKEN
from downloader import mp3_download
from spotify import get_track_name

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a Spotify URL and I'll get the MP3")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if "open.spotify.com/" in url:
        await update.message.reply_text("Fetching the track info...")
        track_name = get_track_name(url)

        if track_name:
            await update.message.reply_text(f" Searching: {track_name}")
            mp3_path = mp3_download(track_name)

            if os.path.exists(mp3_path):
                await update.message.reply_audio(audio=open(mp3_path, 'rb'),title=track_name)
                os.remove(mp3_path)
            else:
                await update.message.reply_text("Failed to download.")
        else:
             await update.message.reply_text("Invalid Spotify URL")
    else:
         await update.message.reply_text("Please Send a Valid URL")

def run():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
    
if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    run()