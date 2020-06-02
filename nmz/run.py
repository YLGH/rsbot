#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

br = (715, 160)

inv_index = []
for i in range(4):
    for j in range(7):
        if i != 0 or j != 0:
            inv_index.append((i,j))

num_overload = 13
num_absorb = 27 - num_overload

overload_index = inv_index[:num_overload]
absorb_index = inv_index[num_overload:]
absorb_index = inv_index

def l_gen(l):
    while True:
        for x in l:
            yield x
        
abs_gen = l_gen(absorb_index)
over_gen = l_gen(overload_index)
PRAYER_LOCATION = (598,148)

for w in range(40000):
    controller.move_mouse_to(PRAYER_LOCATION, delta=0.0)
    controller.click()
    time.sleep(0.25)
    controller.click()

#    for _ in range(num_overload):
#        (i,j) = next(over_gen) 
#        controller.move_mouse_to(controller.inv_location(i,j), duration=0.005)
#        controller.click()
#
#    if w % 5 == 0:
#        for _ in range(num_absorb):
#            (i,j) = next(abs_gen)
#            controller.move_mouse_to(controller.inv_location(i,j), duration=0.005)
#            controller.click()
#

    time.sleep(40)
