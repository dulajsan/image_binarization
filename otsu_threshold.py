import cv2 as cv
import numpy as np


img=cv.imread('images.png',0)

#otsu first round
ret1, thresh =cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow('otsu threshold',thresh)
cv.waitKey(0)
cv.destroyAllWindows();
