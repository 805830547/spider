# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

# set blue thresh
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])

#载入并显示图片
img=cv2.imread(r"C:\Users\Administrator\Desktop\ming.png")
#cv2.imshow('img',img)
#灰度化
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)
#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()