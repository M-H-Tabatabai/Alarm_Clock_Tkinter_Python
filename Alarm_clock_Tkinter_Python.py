import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

alarm_time = None
root = tk.Tk()
root.title("Alarm Clock App")
root.resizable(width=False, height=False)

alarms = []

# Label that shows the current time
time_label = ttk.Label(root, text="12:30:30", font=("Times New Roman", 20))
time_label.place(relx=0.44, rely=0.05, anchor="w")


def get_current_time():
    # Get the current system time
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))

    # Check if any alarm should trigger
    check_alarms(current_time)

    # Update time every second
    root.after(1000, get_current_time)


def set_alarm():
    try:
        # Get hour and minute from user input
        hour = int(hour_alarm_entry.get())
        minute = int(minute_alarm_entry.get())

        now = datetime.now()
        # Create the alarm time for today
        new_alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        # Create a label to show the alarm in the list
        alarm_label = tk.Label(alarm_box, text=new_alarm_time.strftime("%H:%M:%S"),
                               bg="#d0ffd0", font=("Times New Roman", 14))
        alarm_label.pack(pady=5)

        # Save alarm data
        alarms.append({
            "time": new_alarm_time,
            "label": alarm_label
        })

    except ValueError:
        # Show error if input is not valid
        messagebox.showerror("Error", "Invalid time format")


def check_alarms(current_time):
    to_remove = []

    # Check each alarm to see if it's time to trigger
    for alarm in alarms:
        alarm_time = alarm["time"]
        if current_time >= alarm_time:
            # Show alarm popup
            messagebox.showinfo("Alarm", f"Alarm for {alarm_time.strftime('%H:%M:%S')} triggered!")

            # Remove alarm label from UI
            alarm["label"].destroy()

            # Mark alarm for removal
            to_remove.append(alarm)

    # Remove triggered alarms from the list
    for alarm in to_remove:
        alarms.remove(alarm)


# Window size
window_width = 800
window_height = 600

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position for window
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Apply window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Label that displays the digital clock
time_label = ttk.Label(root, text="12:30:30", font=("Times New Roman", 20))
time_label.place(relx=0.44, rely=0.05, anchor="w")

# Hour input field
hour_alarm_entry = ttk.Entry(root, width=20)
hour_alarm_entry.place(relx=0.5, rely=0.45, anchor="center")
label_hour = ttk.Label(root, text="hour", font=("Times New Roman", 20))
label_hour.place(relx=0.1, rely=0.45, anchor="w")

# Minute input field
minute_alarm_entry = ttk.Entry(root, width=20)
minute_alarm_entry.place(relx=0.5, rely=0.55, anchor="center")
label_minute = ttk.Label(root, text="minute", font=("Times New Roman", 20))
label_minute.place(relx=0.1, rely=0.55, anchor="w")

# Button to set alarm
btn_calc = ttk.Button(root, text="Set Alarm", command=set_alarm)
btn_calc.place(relx=0.5, rely=0.65, anchor="center")

# Button to exit the app
btn_close = ttk.Button(root, text="Exit", command=root.destroy)
btn_close.place(relx=0.5, rely=0.9, anchor="center")

# Frame that holds the list of alarms
alarm_box = tk.Frame(root, width=200, height=500)
alarm_box.place(relx=0.85, rely=0.5, anchor="center")

current_alarms = []

# Start updating the clock
get_current_time()

# Run the app
root.mainloop()
