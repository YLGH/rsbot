import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

camelot_teleport = (574, 374)
hialch = (713, 380)
while True:
    controller.mage_book()
    controller.move_mouse_to(camelot_teleport)
    controller.click()
    controller.move_mouse_to(hialch)
    controller.click()
    time.sleep(controller.add_time_noise(1.82))
    controller.click()
    time.sleep(controller.add_time_noise(0.48))


