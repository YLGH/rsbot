from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController

import scipy as scipy
from scipy import interpolate
import time
import numpy as np 

import random

mouse = MouseController()
keyboard = KeyboardController()

def inv_location(x,y):
    INV_00 = (602, 238)
    INV_11 = (645, 275)
    INV_DX = INV_11[0] - INV_00[0]
    INV_DY = INV_11[1] - INV_00[1]

    INV = [ [0 for _ in range(7)] for _ in range(4)]
    for i in range(4):
        for j in range(7):
            INV[i][j] = (INV_00[0] + INV_DX*i, INV_00[1] + INV_DY*j)

    return INV[x][y]


def mage_book():
    keyboard.press(Key.f1)
    time.sleep(0.05)
    keyboard.release(Key.f1)

def get_position():
	return mouse.position

def add_noise_mouse(mouse_position, delta=2):
	[x_noise, y_noise] = np.random.uniform(-delta,delta,2)
	return (mouse_position[0]+x_noise, mouse_position[1]+y_noise)

def add_time_noise(time, noise=0.003):
	[noise] = np.random.uniform(0, noise,1)
	return time+noise

def move_mouse(position_1, position_2, num=400, duration=0.2, delta=3.0):
	(x1,y1) = position_1
	(x2,y2) = position_2

	x = scipy.linspace(x1, x2, num=num, dtype='int')
	y = scipy.linspace(y1, y2, num=num, dtype='int')

	# Move mouse.
	timeout = duration / len(x)
	for (x_, y_) in zip(x,y):
		mouse.position = add_noise_mouse((x_,y_), delta)
		time.sleep(timeout)


def move_mouse_to(position_2, num=400, duration=0.2, delta=3.0):
	(x1,y1) = mouse.position
	(x2,y2) = position_2

	x = scipy.linspace(x1, x2, num=num, dtype='int')
	y = scipy.linspace(y1, y2, num=num, dtype='int')

	# Move mouse.
	timeout = duration / len(x)
	for (x_, y_) in zip(x,y):
		mouse.position = add_noise_mouse((x_,y_), delta)
		time.sleep(timeout)
def move_mouse_relative(x,y, num=400, duration=0.2, delta=3.0):
        move_mouse_to((mouse.position[0]+x, mouse.position[1]+y), num, duration, delta)

def right_click():
	time.sleep(add_time_noise(0.05))
	mouse.press(Button.right)
	time.sleep(add_time_noise(0.05))
	mouse.release(Button.right)

def click():
	mouse.press(Button.left)
	time.sleep(0.05)
	mouse.release(Button.left)
	time.sleep(0.05)
