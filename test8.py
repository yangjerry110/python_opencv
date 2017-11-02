# -*- coding: utf-8 -*-
# @Author: Jerry Yang
# @Date:   2017-11-02 11:55:39
# @Last Modified by:   Jerry Yang
# @Last Modified time: 2017-11-02 15:55:18

import  cv2
import numpy as np

imgName = 'E:\photo\mtest9.jpg'

#调整图片的对比度和亮度
img=cv2.imread(imgName)
cv2.imshow('img',img)
rows,cols,channels=img.shape
dst=img.copy()


a=1.1
b=30
for i in range(rows):
    for j in range(cols):
        for c in range(3):
            color=img[i,j][c]*a+b
            if color>255:
                dst[i,j][c]=255
            elif color<0:
                dst[i,j][c]=0

cv2.imshow('dst',dst)
cv2.waitKey(0)

#对图片实现高斯模糊
kernel_size = (3, 3);
sigma = 0;

gaosi = cv2.GaussianBlur(dst, kernel_size, sigma);
#new_imgName = "New_" + str(kernel_size[0]) + "_" + str(sigma) + "_" + imgName;

cv2.imshow("gaosi",gaosi)
cv2.waitKey(0)

#整体磨皮
#双边模糊系数
bilateralFilterVal = 30

mop = cv2.bilateralFilter(gaosi,bilateralFilterVal,bilateralFilterVal*2,bilateralFilterVal/2) 

cv2.imshow("mop",mop)
cv2.waitKey(0)

#图像增强
"""
final_size = (0,0)
final_sigma = 9
final = cv2.GaussianBlur(gaosi,final_size,final_sigma)
"""
finalImg = cv2.addWeighted(mop,0.9,img,0.5,0)
cv2.imshow("final",finalImg)
cv2.waitKey(0)

cv2.destroyAllWindows()
