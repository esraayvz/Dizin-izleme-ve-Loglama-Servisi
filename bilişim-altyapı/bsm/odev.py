import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher:
    DIRECTORY_TO_WATCH = "/home/ubuntu/bsm/test"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH,recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None
        else:
            log_data = {
                "event_type": event.event_type,
                "src_path": event.src_path
            }
            log_path = "/home/ubuntu/bsm/logs/changes.json"
            with open(log_path, 'a') as log_file:
                log_file.write(json.dumps(log_data) + "\n")

if __name__ == "__main__":
    watcher = Watcher()
    watcher.run()
