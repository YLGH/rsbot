#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

from pynput import keyboard



def on_press(key):
    if hasattr(key, 'char'):
        if key.char == 'z':
            controller.right_click()
            controller.move_mouse_relative(0,90, duration = 0.009)
            controller.click()
            controller.move_mouse_relative(0,-90, duration = 0.009)
        if key.char == 'x':
            controller.right_click()
            controller.move_mouse_relative(0,60, duration = 0.009)
            controller.click()
            controller.move_mouse_relative(0,-60, duration = 0.009)
            
            

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

