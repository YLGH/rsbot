import pyscreenshot
import numpy as np
from PIL import Image
import cv2
import sys
import controller
import time

# floor token 1 385 280 -> 380 275

location_to_image = {}
for roof_index in range(1,8):
	key = "roof"+str(roof_index)+".png"
	location_to_image[key] = np.asarray(cv2.imread(key))
for floor_index in [1,2,3]:
	key = "floor"+str(floor_index)+".png"
	location_to_image[key] = np.asarray(cv2.imread(key))
# for roof_token_index in [1,2,4,5]:
# 	key = "roof"+str(roof_token_index)+"token.png"
# 	location_to_image[key] = np.asarray(cv2.imread(key))

for key in ["roof6stuck.png", "roof1stuck.png"]:
	location_to_image[key] = np.asarray(cv2.imread(key))

def floor1action():
	controller.move_mouse(controller.get_position(), (350,255))
	controller.click()
	time.sleep(controller.add_time_noise(7.0))
def floor2action():
	controller.move_mouse(controller.get_position(), (755,186), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(8))
	controller.move_mouse(controller.get_position(), (533,348), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(8))
def floor3action():
	controller.move_mouse(controller.get_position(), (400,165), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(10))

def roof1tokenaction():
	controller.move_mouse(controller.get_position(), (387,280))
	controller.click()
	time.sleep(controller.add_time_noise(1.85))
	controller.move_mouse(controller.get_position(), (380,277))
	controller.click()
	time.sleep(controller.add_time_noise(3.7))

def roof2tokenaction():
	controller.move_mouse(controller.get_position(), (370,311))
	controller.click()
	time.sleep(controller.add_time_noise(1.1))
	controller.move_mouse(controller.get_position(), (310,340))
	controller.click()
	time.sleep(controller.add_time_noise(4.2))

def roof3tokenaction():
	controller.move_mouse(controller.get_position(), (352,369),delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(2.1))
	controller.move_mouse(controller.get_position(), (308,352), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(4.6))


def roof4tokenaction():
	controller.move_mouse(controller.get_position(), (366,364),delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(1.8))
	controller.move_mouse(controller.get_position(), (382,394))
	controller.click()
	time.sleep(controller.add_time_noise(3.8))


def roof5tokenaction():
	controller.move_mouse(controller.get_position(), (384,351), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(1.4))
	controller.move_mouse(controller.get_position(), (416,340 ), delta=1)
	controller.click()
	time.sleep(controller.add_time_noise(6.9))

def roof1action():
	return roof1tokenaction()
def roof2action():
	return roof2tokenaction()
def roof3action():
	return roof3tokenaction()
def roof4action():
	return roof4tokenaction()
def roof5action():
	return roof5tokenaction()
def roof6action():
	controller.move_mouse(controller.get_position(), (618,323))
	controller.click()
	time.sleep(controller.add_time_noise(7.05))
def roof7action():
	controller.move_mouse(controller.get_position(), (385,230))
	controller.click()
	time.sleep(controller.add_time_noise(4.4))

def roof6stuckaction():
	controller.move_mouse(controller.get_position(), (745,153), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(5.2))
	controller.move_mouse(controller.get_position(), (410,320), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(3.0))

def roof1stuckaction():
	controller.move_mouse(controller.get_position(), (690,116), delta=0.0)
	controller.click()
	time.sleep(controller.add_time_noise(3.2))
	controller.move_mouse(controller.get_position(), (378,308))
	controller.click()
	time.sleep(controller.add_time_noise(4.55))

possible_next = {
	"roof1.png" : ["roof2.png"],
	"roof2.png" : ["roof3.png"],
	"roof3.png" : ["roof4.png", "floor2.png"],
	"roof4.png" : ["roof5.png"],
	"roof5.png" : ["roof6.png", "roof6stuck.png"],
	"roof6.png" : ["roof7.png", "floor3.png"],
	"roof7.png" : ["floor1.png"],

	"floor1.png" : ["roof1.png", "roof1stuck.png"],
	"floor2.png" : ["roof1.png", "roof1stuck.png"],
	"floor3.png" : ["roof1.png", "roof1stuck.png", "floor3.png"],

	"roof6stuck.png" : ["roof7.png"],
	"roof1stuck.png" : ["roof2.png"]
}

location_to_action = {
	"roof1.png" : roof1action,	
	"roof2.png" : roof2action,
	"roof3.png" : roof3action,
	"roof4.png" : roof4action,
	"roof5.png" : roof5action,
	"roof6.png" : roof6action,
	"roof7.png" : roof7action,

	"floor1.png" : floor1action,
	"floor2.png" : floor2action,
	"floor3.png" : floor3action,

	# "roof1token.png" : roof1tokenaction,
	# "roof2token.png" : roof2tokenaction,
	# "roof4token.png" : roof4tokenaction,
	# "roof5token.png" : roof5tokenaction,

	"roof6stuck.png" : roof6stuckaction,
	"roof1stuck.png" : roof1stuckaction


}

import sys
last_state = None
if len(sys.argv) > 1:
	last_state = sys.argv[1] + ".png"


while True:

	screenshot = pyscreenshot.grab(bbox=(0,70,720,500))
	# screenshot.save("floor1.png")
	# sys.exit(0)

	screen_np = np.asarray(screenshot)
	screen_np = np.delete(screen_np, -1, axis=-1)

	min_location = None
	min_value = 1000000
	if last_state == None:
		next_possible = location_to_image.keys()
	else:
		next_possible = possible_next[last_state] + [last_state]
	for location_key in next_possible:
		location_image = location_to_image[location_key]
		diff = np.square(np.subtract(location_image, screen_np)).mean()
		if diff < min_value:
			min_value = diff
			min_location = location_key


	print(min_value, min_location)
	last_state = min_location
	location_to_action[min_location]()

