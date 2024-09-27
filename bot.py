from telegram import Update
from telegram.ext import Application, CommandHandler
import threading
from GUI import game_gui  # Import GUI
import database  # Import the database module

API_TOKEN = '7773928774:AAEA60tg3ZmtwVLXF2iLJBKT80bR00pvEtM'

# /start command
async def start(update: Update, context) -> None:
    """Send a message when the command /start is issued."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    
    # Check if user exists in the database
    user = database.get_user(user_id)
    
    if user is None:
        # Add new user if not already in the database
        database.add_user(user_id, username)
        await update.message.reply_text(f"Welcome to $TinubuCoin, {username}! Your account has been created.")
    else:
        await update.message.reply_text(f"Welcome back, {username}! You already have an account.")

    # Run the GUI in a separate thread
    threading.Thread(target=game_gui.main).start()

async def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(API_TOKEN).build()

    # Initialize the application before starting
    await application.initialize()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.start()
    print("Bot is running...")

    # Keep the bot running until it’s stopped
    await application.updater.start_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
