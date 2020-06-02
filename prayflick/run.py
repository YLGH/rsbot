#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

PRAYER_LOCATION = (598,148)


for w in range(40000):
    controller.click()
    controller.click()
    time.sleep(.38)
