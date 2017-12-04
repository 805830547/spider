# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:15:39 2017

@author: tina
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#载入并显示图片
img=cv2.imread(r"C:\Users\Administrator\Desktop\ming.png")
#cv2.imshow('img',img)
#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(
    gray,cv2.HOUGH_GRADIENT,1,6,param1=100,param2=29,minRadius=5,maxRadius=15)
#输出返回值，方便查看类型
#print(circles)
#输出检测到圆的个数
print(len(circles[0]))

print('-------------我是条分割线-----------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    #print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    print('圆心:(' + str(circle[0]) + ', ' + str(circle[1]) + '), 半径:' + str(circle[2]) + ', 颜色:' + str(img[x,y]))
    #半径
    r=int(circle[2])
    #在原图用指定颜色标记出圆的位置
    img=cv2.circle(img,(x,y),r,(0,0,0),1)
    img =cv2.line(img, (x, y - r), (x, y + r), (0,0,0), 1)
    '''
#显示新图像
#cv2.namedWindow("ming", 0);
#cv2.resizeWindow("ming", 640, 480);
cv2.imshow('ming',img)

#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
