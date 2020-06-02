import pyscreenshot
import numpy as np
from PIL import Image, ImageFilter
import cv2
import sys
import controller
import time
import pytesseract as pt


(562, 110)
(580, 125)

position = controller.get_position()
controller.right_click()
img = pyscreenshot.grab(bbox=(position[0]-140,position[1]+5, position[0]+140, position[1]+35))
img.save('pickpocket.png')

#def hitpoints():
#    img = pyscreenshot.grab(bbox=(562,110,580,125))
#    new_size = tuple(6*x for x in img.size)
#    img = img.resize(new_size, Image.ANTIALIAS)
#    print(pt.image_to_string(img, config='-c tessedit_char_whitelist=0123456789 --oem 0'))
#    img.show()
#    
#hitpoints()
