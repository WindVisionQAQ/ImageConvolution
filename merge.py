#! /usr/bin/python
import cv2
import numpy
import pandas as pd
 
img=cv2.imread("3.png")
img0=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=open('d4.txt')
lines=f.readlines()
row=0
for line in lines:
	list = line.strip('\n').split(' ')
	img0[row:] = list[0:]
	row = row + 1
f.close()

cv2.imshow("Image",img0)
cv2.waitKey(0)