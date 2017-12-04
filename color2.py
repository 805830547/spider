# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

# set blue thresh
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])

#载入并显示图片
img=cv2.imread(r"C:\Users\Administrator\Desktop\ming3.png")
x = 24
y = 95
(b, g, r) = img[y, x]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b)) #13
img = cv2.circle(img, (x, y), 3, (int(b), int(g), int(r)), -1)
#cv2.namedWindow("ming", 0);
cv2.imshow('ming', img)
#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()