#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time
import random
import numpy as np



br = (600, 240)


for w in range(40000):
    if w % 10 == 0:
        start_position = controller.get_position()
        controller.move_mouse_to(br)
        controller.click()
        time.sleep(0.0005 + np.random.uniform(-.0001, .0001))
        controller.click()
        controller.move_mouse_to(start_position)
    
    controller.click()
    time.sleep(0.0005 + np.random.uniform(-.0001, .0001))
    controller.click()
    time.sleep(0.6 + np.random.uniform(-.0001, .0001))
