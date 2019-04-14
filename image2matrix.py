#! /usr/bin/python
import cv2
import numpy
import pandas as pd
img=cv2.imread("3.png")
b,g,r=cv2.split(img)
f = open("blue.txt","w")
f1 = open("green.txt","w")
f2 = open("red.txt","w")
for i in range(1024):
	for j in range(2048):
		f.write(str(b[i][j]))
		f.write(' ')
		f1.write(str(g[i][j]))
		f1.write(' ')
		f2.write(str(r[i][j]))
		f2.write(' ')
	f.write('\n')
	f1.write('\n')
	f2.write('\n')
f.close()
f1.close()
f2.close()
print (b.shape)
print (b)
print (g)
print (r)

