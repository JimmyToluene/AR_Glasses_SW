from pynput import keyboard
from pynput.keyboard import Key


def on_press(key):
    #handle pressed keys
    pass

def on_release(key):
    #handle released keys
    if(key==Key.enter):
        function_x()

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()