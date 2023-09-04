import time
import win32gui
from PIL import ImageGrab


def capture():
    screenshot = ImageGrab.grab()
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"../images/{timestamp}.png"
    screenshot.save(filename)
    print(f"Ekran görüntüsü kaydedildi: {filename}")


def take_screenshots(interval=180):
    active_window = None
    previous_title = None
    start_time = time.time()
    while True:
        # it takes a screenshot every 3 minutes for better analysis, interval is customizable.
        current_time = time.time()
        if current_time - start_time >= interval:
            capture()
            start_time = current_time

        foreground_window = win32gui.GetForegroundWindow()
        if foreground_window != active_window:
            active_window = foreground_window
            window_title = win32gui.GetWindowText(active_window)
            if window_title != previous_title:
                capture()
                previous_title = window_title
        time.sleep(1)


take_screenshots()
