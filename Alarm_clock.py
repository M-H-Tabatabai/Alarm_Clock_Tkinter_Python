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

#lable show clock
label_clock_now = ttk.Label(root, text="12:30:30", font=("Times New Roman", 20))
label_clock_now.place(relx=0.44, rely=0.05, anchor="w")

#entey and lable hour
entry_hour = ttk.Entry(root, width=20)
entry_hour.place(relx=0.5, rely=0.45, anchor="center")
label_hour = ttk.Label(root, text="hour", font=("Times New Roman", 20))
label_hour.place(relx=0.1, rely=0.45, anchor="w")

#entry and lable minute
entry_minute = ttk.Entry(root, width=20)
entry_minute.place(relx=0.5, rely=0.55, anchor="center")
label_minute = ttk.Label(root, text="minute", font=("Times New Roman", 20))
label_minute.place(relx=0.1, rely=0.55, anchor="w")

root.mainloop()