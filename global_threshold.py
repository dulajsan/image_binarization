import cv2 as cv
import numpy as np


#method 1 - global  thresold

#read the image , 2nd parameter- cv.IMREAD_GRAYSCALE
img=cv.imread('OpenCV_Logo.png',0)
ret,thresh=cv.threshold(img,127,255,cv.THRESH_BINARY)



#display an image in a window
cv.imshow('global threshold',thresh)
cv.waitKey(0)
cv.destroyAllWindows()
