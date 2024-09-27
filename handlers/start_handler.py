from telegram import Update
from telegram.ext import CallbackContext
from database import connect_db

# Register the user in the database if they don't exist
def register_user(user_id, username):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Check if the user already exists
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    # If the user doesn't exist, create a new entry
    if not user:
        cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()

    conn.close()

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username

    # Register the user in the database
    register_user(user_id, username)
    
    await update.message.reply_text(f"Welcome to $TinubuCoin, {username}! You are now registered.")
