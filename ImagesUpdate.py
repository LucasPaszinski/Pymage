# need to pip install
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

import codegenerator.ImagesCodeGenerator as Gen


# When this is running any changes in folder ..\Images will trigger an
# Gen.Run() to update Images class

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        Gen.Run()
        return super().on_any_event(event)


folder_to_track = os.path.join(os.path.dirname(__file__), 'Images')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
