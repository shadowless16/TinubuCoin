from telegram import Update
from telegram.ext import CallbackContext
from database import connect_db

# Function to get a user's shege balance
def get_shege(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT shege FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else 0

# /balance command to check current shege balance
async def balance(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    current_shege = get_shege(user_id)

    await update.message.reply_text(f"Your current shege balance is: {current_shege:.2f}")
