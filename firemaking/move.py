#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

INV_00 = (582, 278)
INV_11 = (626, 314)
INV_DX = INV_11[0] - INV_00[0]
INV_DY = INV_11[1] - INV_00[1]

INV = [ [0 for _ in range(7)] for _ in range(4)]
LOGS = []
for i in range(4):
    for j in range(7):
        INV[i][j] = (INV_00[0] + INV_DX*i, INV_00[1] + INV_DY*j)
        if (i,j) not in [(0,3), (2,3)]:
            LOGS.append(INV[i][j])

LOGS_1 = LOGS[:13]
LOGS_2 = LOGS[13:]
log_index = 0

TBOX = INV[2][3]

NEXT = (500, 306)

from pynput import keyboard

def make_left():
    for log_index in range(13):
        controller.move_mouse_to(TBOX, duration = 0.009, delta=0.0)
        controller.click()

        controller.move_mouse_to(LOGS_2[log_index], duration = 0.009, delta=0.0)
        controller.click()

        if log_index == 0:
            time.sleep(2.2)
        else:
            time.sleep(1.6)

def on_press(key):
    global log_index
    if hasattr(key, 'char'):
        if key.char == 'z':
            controller.move_mouse_to(TBOX, duration = 0.009, delta=0.0)
            controller.click()
        if key.char == 'x':
            controller.move_mouse_to(LOGS[log_index], duration = 0.009, delta=0.0)
            log_index += 1
            log_index %= len(LOGS)
            controller.click()
        if key.char == 'c':
            controller.move_mouse_to(NEXT, duration = 0.009, delta=0.0)
            controller.click()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

