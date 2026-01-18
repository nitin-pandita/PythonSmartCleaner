# 🧹 Desktop Cleaner Automator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/Library-Watchdog-green?style=for-the-badge)](https://pypi.org/project/watchdog/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?style=for-the-badge)](https://github.com/)

> **Stop the chaos.** Automatically organize your Desktop files into clean folders the moment they are created.

---

## 🧐 What is this?

We've all been there: you download a PDF, save a screenshot, and unzip a file. Suddenly, your Desktop is a war zone of icons.

**Desktop Cleaner Automator** is a lightweight Python background service that:

1.  **Watches** your Desktop in real-time.
2.  **Detects** new files instantly.
3.  **Sorts** them into categorized folders (Images, PDFs, Videos, etc.).

It’s like having a personal assistant who tidies up your desk while you work. 🧹✨

---

## 🚀 Features

- **⚡ Real-Time Monitoring:** Uses `watchdog` to detect file events instantly.
- **📂 Smart Sorting:** Automatically groups files by extension (e.g., `.jpg` → `Image Files`).
- **🛡️ Fail-Safe:** Includes logic to wait for file transfers to finish before moving (prevents corruption).
- **⚙️ Fully Customizable:** easily add your own file extensions and folder names.

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone [https://github.com/yourusername/desktop-cleaner.git](https://github.com/yourusername/desktop-cleaner.git)
cd desktop-cleaner
```

2. Install Dependencies
   You only need one external library for the magic to happen:

pip install watchdog

3. Run the Script
   python cleaner.py

You should see a message confirming that monitoring has started:

🚀 Monitoring: /Users/YourName/Desktop
