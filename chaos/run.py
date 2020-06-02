#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

wilder=(720,300)

from pynput import keyboard

def on_press(key):
    if hasattr(key, 'char'):
        if key.char == 'z':
            controller.right_click()
            controller.move_mouse_relative(0,40, duration = 0.001)
            controller.click()
        if key.char == 'x':
            curr = controller.get_position()
            curr = (curr[0], curr[1]-40)
            controller.move_mouse_to(wilder, duration = .0001)
            controller.click()
            controller.move_mouse_to(curr, duration = .0001)

def on_release(key):
    if key == keyboard.Key.esc:
        return True
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

