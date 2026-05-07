import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

alarm_time = None
root = tk.Tk()
root.title("Alarm Clock App")
root.resizable(width=False, height=False)

time_label = ttk.Label(root, text="12:30:30", font=("Times New Roman", 20))
time_label.place(relx=0.44, rely=0.05, anchor="w")

def get_current_time():
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    root.after(1000, get_current_time)

def set_alarm():
    global alarm_time
    current_time = datetime.now()
    alarm_time = current_time.replace(hour=int(hour_alarm_entry.get()), minute=int(
        minute_alarm_entry.get()), second=0, microsecond=0)
    latest_alarm_label.configure(text=alarm_time.strftime("%H:%M:%S"))



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

# lable show clock
time_label = ttk.Label(root, text="12:30:30", font=("Times New Roman", 20))
time_label.place(relx=0.44, rely=0.05, anchor="w")

# entey and lable hour
hour_alarm_entry = ttk.Entry(root, width=20)
hour_alarm_entry.place(relx=0.5, rely=0.45, anchor="center")
label_hour = ttk.Label(root, text="hour", font=("Times New Roman", 20))
label_hour.place(relx=0.1, rely=0.45, anchor="w")

# entry and lable minute
minute_alarm_entry = ttk.Entry(root, width=20)
minute_alarm_entry.place(relx=0.5, rely=0.55, anchor="center")
label_minute = ttk.Label(root, text="minute", font=("Times New Roman", 20))
label_minute.place(relx=0.1, rely=0.55, anchor="w")

latest_alarm_label = tk.Label(root, text='No alarm has been set')
latest_alarm_label.place(relx=0.75, rely=0.65, anchor="center")

# button set alarm
btn_calc = ttk.Button(root, text="Set Alarm", command=set_alarm)
btn_calc.place(relx=0.5, rely=0.65, anchor="center")

# Exit Button
btn_close = ttk.Button(root, text="Exit", command=root.destroy)
btn_close.place(relx=0.5, rely=0.9, anchor="center")

get_current_time()
root.mainloop()
