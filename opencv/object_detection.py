import cv2
import numpy as np
from matplotlib import pyplot as plt


# region object detection hsv
def nothing(x):
    pass

cv2.namedWindow('track datas')
cv2.createTrackbar('LH', 'track datas',0,255,nothing)
cv2.createTrackbar('LS', 'track datas',0,255,nothing)
cv2.createTrackbar('LV', 'track datas',0,255,nothing)
cv2.createTrackbar('UH', 'track datas',255,255,nothing)
cv2.createTrackbar('US', 'track datas',255,255,nothing)
cv2.createTrackbar('UV', 'track datas',255,255,nothing)
cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    # img = cv2.imread("baloons.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('LH','track datas')
    l_s = cv2.getTrackbarPos('LS','track datas')
    l_v = cv2.getTrackbarPos('LV','track datas')
    u_h = cv2.getTrackbarPos('UH', 'track datas')
    u_s = cv2.getTrackbarPos('US', 'track datas')
    u_v = cv2.getTrackbarPos('UV', 'track datas')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('hasbullah', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
# endregion


# region Morphological Transformations
baloon = cv2.imread("baloons.jpg", 0)
_, mask = cv2.threshold(baloon,220,255, cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal , iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernal) #first erosion, then dilation is applied
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal) #reverse of MORPH_OPEN

titles = ['Original Image', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [baloon, mask, dilation, erosion, opening,closing]
for i in range(6):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# endregion



