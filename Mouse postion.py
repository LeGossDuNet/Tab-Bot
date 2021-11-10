import pynput.mouse
from pynput import keyboard

mouse = pynput.mouse.Controller()

def on_press(key):
    print("")


def on_release(key):
    print("")
    if key == keyboard.Key.space:
        print(mouse.position)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()