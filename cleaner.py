import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

home_directory = os.path.expanduser("~")
folder_to_track = os.path.join(home_directory, "Downloads")

EXTENSION_MAP = {
    ".pdf": "PDF Files",
    ".jpg": "Image Files",
    ".jpeg": "Image Files",
    ".png": "Image Files",
    ".gif": "Image Files",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".xls": "Excel Sheets",
    ".xlsx": "Excel Sheets",
    ".zip": "Archives",
    ".mov": "Videos",
    ".mp4": "Videos",
}

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        _, extension = os.path.splitext(file_path)
        file_name = os.path.basename(file_path)
        folder_path = os.path.dirname(file_path)

        extension = extension.lower()

        if extension in EXTENSION_MAP:
            time.sleep(2)  # important for CapCut exports

            category = EXTENSION_MAP[extension]
            destination_folder = os.path.join(folder_path, category)
            os.makedirs(destination_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(destination_folder, file_name))
                print(f"Moved: {file_name} → {category}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(MyHandler(), folder_to_track, recursive=False)
    observer.start()

    print("🎬 Monitoring  ... Ctrl+C to stop")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
