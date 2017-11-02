# -*- coding: utf-8 -*-
# @Author: Jerry Yang
# @Date:   2017-11-02 17:15:20
# @Last Modified by:   Jerry Yang
# @Last Modified time: 2017-11-02 17:51:50

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('E:\photo\mtest.jpg') #直接读为灰度图像

#展示img
cv2.imshow("1",img)
cv2.waitKey(0)

blur = img.copy()

for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    blur[temp_x][temp_y] = 255

#9---滤波领域直径
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
#blur = cv2.bilateralFilter(img,9,75,75)
#$plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
#plt.subplot(1,2,2),plt.imshow(blur,'gray')


#展示blur
cv2.imshow("2",blur)
#展示时间
cv2.waitKey(0)

test3 = cv2.medianBlur(blur,3)
cv2.imshow('3',test3)
cv2.waitKey(0)

cv2.destroyAllWindows()