import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Alarm Clock App")
root.resizable(width=False, height=False)

# Center the window on the screen
window_width = 800
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x, y position for centering
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Apply window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")



root.mainloop()