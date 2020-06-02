import sys
sys.path.insert(0, '/Users/yingliu/Desktop/rsbot')
import controller
import time

use_bank = (395, 361)
deposit = (460, 364)

harralander_unf = (200, 140)
goat_horn_dust = (150, 140)
exit = (500, 70)

use_harralander = (640, 350)
use_goat_horn = (640, 380)

make_all = (272, 528)

while True:
    controller.move_mouse_to(use_bank, duration=0.52)
    controller.click()

    time.sleep(1)

    controller.move_mouse_to(deposit, duration=0.52)
    controller.click()

    controller.move_mouse_to(harralander_unf, duration=0.52)
    controller.click()

    controller.move_mouse_to(goat_horn_dust, duration=0.52)
    controller.click()

    controller.move_mouse_to(exit, duration=0.3)
    controller.click()

    controller.move_mouse_to(use_harralander, duration=0.52)
    controller.click()

    controller.move_mouse_to(use_goat_horn, duration=0.52)
    controller.click()

    controller.move_mouse_to(make_all, duration=0.55)
    controller.click()

    time.sleep(controller.add_time_noise(18.2))


