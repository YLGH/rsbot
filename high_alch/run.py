import pyscreenshot
import numpy as np
from PIL import Image
import cv2
import sys

sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time



while True:
    controller.move_mouse(controller.get_position(), (742, 289))
    controller.click()
    time.sleep(controller.add_time_noise(0.5))
    controller.move_mouse(controller.get_position(), (731, 271))
    controller.click()
    time.sleep(controller.add_time_noise(0.9))
    controller.move_mouse(controller.get_position(), (692, 289))
    controller.click()
    time.sleep(controller.add_time_noise(2.4))
