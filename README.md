## About the Project

This project includes an application that records keyboard inputs and captures screenshots. The application is divided into two main modules:

### Keylogger Module (`keylogger.py`)

The Keylogger module is responsible for recording keyboard inputs. It captures key presses and clipboard content. It also handles special keys such as Enter, Backspace, and Caps Lock. The logged data is saved to the `keyboard_entries.txt` file.

### Screenshot Capture Module (`screenshot.py`)

The Screenshot Capture module captures screenshots at regular intervals and when the active window changes. The captured screenshots are saved in the `images/` directory with timestamps.

## Files and Folders

The project files and folders are as follows:

- `main.py`: The main application file.
- `modules/`: The folder where modules are located.
  - `keylogger.py`: Module for recording keyboard inputs.
  - `screenshot.py`: Module for capturing screenshots.
- `images/`: The folder where captured screenshots are stored.

## Usage

You can follow these steps to run the project:

1. Create a folder named `images`. This folder will be used to store the captured screenshots.

2. Run the `main.py` file. This will start the keyboard logger and screenshot taker.

3. Record keyboard inputs and capture screenshots. Keyboard logs will be saved in the `keyboard_entries.txt` file.

4. To terminate the program, you can use the `end` key on the keyboard.

## Requirements

The project requires the following dependencies:

- Python
- Pynput
- Pyperclip
- Win32gui
- PIL (Python Imaging Library)
- Keyboard (for listening to keyboard keys)

You can install these requirements by running the following commands in the terminal:
  pip install pynput pyperclip pywin32 pillow keyboard


