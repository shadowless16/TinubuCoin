import sqlite3
import logging

# Set up database connection (ensure you have a users table created in your database)
conn = sqlite3.connect('tinubucoin_db.sqlite3', check_same_thread=False)  # Adjust the path to your database file
cursor = conn.cursor()

# Set up logging to log user creation events
logging.basicConfig(filename='user_creation.log', level=logging.INFO)

# Function to create the users table (you only need to run this once when initializing the database)
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            username TEXT NOT NULL
        )
    ''')
    conn.commit()

# Function to add a new user to the database
def add_user(user_id, username, profile_photo_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, username, profile_photo_id) VALUES (?, ?, ?)', (user_id, username, profile_photo_id))
    conn.commit()
    conn.close()

# Function to check if a user exists in the database
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

# Function to list all users in the database (for debugging purposes)
def list_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Optional: Call create_table if you're running the script to initialize the table
create_table()

# Example usage for testing (you can remove these lines in production)
if __name__ == '__main__':
    # Add a test user
    add_user(12345, 'testuser')
    
    # Check if the test user exists
    user = get_user(12345)
    if user:
        print(f"Found user: {user}")
    
    # List all users
    list_all_users()
