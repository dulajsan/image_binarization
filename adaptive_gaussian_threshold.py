import cv2 as cv
import numpy as np


img=cv.imread('noisy_text.jpg',0)
thresh=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow('adaptive threshold',thresh)
cv.waitKey(0)
cv.destroyAllWindows();
