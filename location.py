#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

#判断小球颜色
def get_color_name(r, g, b):
    #red
    if 250 < r and r <=255 and 60 < g and g <=70 and 60 < b and b <=70:
        return (0, 0, 255)#'red'
    elif 60 < r and r <=70 and 195 < g and g <=205 and 250 < b and b <=255:
        return (255, 0, 0)#'blue'
    elif 250 < r and r <=255 and 180 < g and g <=245 and 60 < b and b <=90:
        return (0, 255, 255)#'yellow'
    else:
        return (255, 255, 255)#'gray'

# 判断小球颜色
def get_color_type(r, g, b):
    # red
    if 250 < r and r <= 255 and 60 < g and g <= 70 and 60 < b and b <= 70:
        return 'RED'
    elif 60 < r and r <= 70 and 195 < g and g <= 205 and 250 < b and b <= 255:
        return 'BLUE'
    elif 250 < r and r <= 255 and 180 < g and g <= 245 and 60 < b and b <= 90:
        return 'YELLOW'
    else:
        return 'GRAY'
#载并显示图片
img=cv2.imread(r"C:\Users\Administrator\Desktop\ming.png")
for i in range(14):
    for j in range(32):
        x = 24 + 24 * j
        y = 95 + 64 * i
        (b, g, r) = img[y, x]
        '''
        print(str((r, g, b)))
        type = get_color_type(int(r), int(g), int(b))
        if (type == 'RED'):
            print('red button click')
        elif (type == 'BLUE'):
            print('blue button click')
        elif (type == 'YELLOW'):
            print('both button click==================')
        elif (type == 'GRAY'):
            print('delay some time')
        '''
        #颜色 b, g, r
        img = cv2.circle(img, (x, y + 32), 5, get_color_name(int(r), int(g), int(b)), -1)
cv2.namedWindow("ming", 0);
cv2.imshow('ming', img)
#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()

