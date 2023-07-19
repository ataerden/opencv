import cv2
import numpy as np


img = cv2.imread('images/seperated_baloons.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,200,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0,0,0), 3)

cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





