import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("$TinubuCoin Game")
    root.geometry("400x600")  # Adjust the size of the window

    # Load Tinubu's image and display in the center
    tinubu_image = Image.open("GUI/assets/tinubu.png")  # Update this path as needed
    tinubu_image = tinubu_image.resize((150, 150), Image.LANCZOS)
    tinubu_photo = ImageTk.PhotoImage(tinubu_image)

    # Label for Tinubu's face
    tinubu_label = tk.Label(root, image=tinubu_photo)
    tinubu_label.pack(pady=20)

    # Shege per hour label
    shege_per_hour = tk.Label(root, text="Shege per hour: +7.39", font=("Helvetica", 16))
    shege_per_hour.pack(pady=10)

    # Section for daily rewards
    daily_combo_label = tk.Label(root, text="Daily Combo", font=("Helvetica", 14))
    daily_combo_label.pack(pady=10)

    # Buttons for games or actions
    button1 = tk.Button(root, text="Count Masters", width=20, height=2)
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Merge Away", width=20, height=2)
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Train Miner", width=20, height=2)
    button3.pack(pady=5)

    # Display the current Shege balance
    balance_label = tk.Label(root, text="Your balance: 59.49 Shege", font=("Helvetica", 16))
    balance_label.pack(pady=10)

    # Main loop to run the application
    root.mainloop()

if __name__ == '__main__':
    main()
