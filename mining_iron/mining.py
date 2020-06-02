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


def add_noise_mouse(mouse_position, delta):
	[x_noise, y_noise] = np.random.uniform(-delta,delta,2)
	return (mouse_position[0]+x_noise, mouse_position[1]+y_noise)

def add_time_noise(time, noise=0.005):
	[noise] = np.random.uniform(0, noise,1)
	return time+noise

def move_mouse(position_1, position_2, num=400, duration=0.2):
	(x1,y1) = position_1
	(x2,y2) = position_2

	x = scipy.linspace(x1, x2, num=num, dtype='int')
	y = scipy.linspace(y1, y2, num=num, dtype='int')

	# Move mouse.
	timeout = duration / len(x)
	for (x_, y_) in zip(x,y):
		mouse.position = add_noise_mouse((x_,y_), 5.0)
		time.sleep(timeout)

def click():
	mouse.press(Button.left)
	time.sleep(add_time_noise(0.05))
	mouse.release(Button.left)