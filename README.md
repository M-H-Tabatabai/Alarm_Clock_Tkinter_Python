# ⏰ Alarm Clock App (Python Tkinter)

A simple and elegant **Alarm Clock Desktop Application** built with **Python** and **Tkinter**.  
This app shows a **live digital clock** and allows users to **set multiple alarms** that trigger a popup notification at the scheduled time.

Perfect for beginners learning **GUI programming in Python**.

---

## ✨ Features

✅ Live digital clock (updates every second)  
✅ Set alarms using hour and minute input  
✅ Supports **multiple alarms simultaneously**  
✅ Visual list of active alarms  
✅ Popup notification when alarm triggers  
✅ Clean Tkinter GUI interface  
✅ Simple and beginner‑friendly code

---

## 🖥️ Preview

```
+--------------------------------------+
|              14:32:18                |
|                                      |
|  hour      [        ]                |
|  minute    [        ]                |
|                                      |
|           [ Set Alarm ]              |
|                                      |
|                   Active Alarms      |
|                   15:00:00           |
|                   16:30:00           |
|                                      |
|                [ Exit ]              |
+--------------------------------------+
```

---

## 🧠 How It Works

The application performs three main tasks:

| Component | Description |
|-----------|-------------|
| ⏱ Live Clock | Updates every second using `root.after(1000, function)` |
| 🔔 Alarm Storage | Alarms are stored in a Python list containing time and UI label |
| 📢 Alarm Trigger | Each second the program checks if the current time matches an alarm |

When the time matches:

1. A popup message appears  
2. The alarm is removed from the list  
3. The alarm label disappears from the UI

---

## 📦 Requirements

Make sure Python is installed.

Python Version Recommended:

```
Python 3.8+
```

Libraries used:

```
tkinter
datetime
```

These come **preinstalled with Python**, so no additional installation is required.

---


## 🎯 Example Usage

1. Enter the **hour** (24‑hour format)
2. Enter the **minute**
3. Click **Set Alarm**
4. The alarm appears in the list
5. When time matches → a popup alert appears

Example:

```
Hour:   14
Minute: 45
Alarm:  14:45:00
```

---

## 🛠️ Built With

- 🐍 **Python**
- 🖼 **Tkinter GUI Toolkit**
- ⏳ **Datetime module**

---

## 💡 Future Improvements

Possible upgrades for the project:

- 🔊 Alarm sound notification
- 🗑 Delete specific alarms
- ⏰ 12‑hour format option
- 🎨 Improved UI styling
- 📅 Date-based alarms
- 💾 Save alarms between sessions

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

mohammad hossein

If you like this project ⭐ consider starring the repository!

---

## 📜 License

This project is open source and available under the **MIT License**.

---

⏰ *Never miss an important moment again!*
