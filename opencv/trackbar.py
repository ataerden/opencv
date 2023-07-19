import cv2
import numpy as np
h = 0
w = 0

def h1(x):
    h = x
def w1(x):
    w = x


img = cv2.imread("images/hasbullah.PNG", 1)
cv2.namedWindow('hasbullah')
height, width = img.shape[:2]
print(width)
switch = "ON/OFF"
cv2.namedWindow('tracking')
cv2.createTrackbar('height', 'tracking',0,height,h1)
cv2.createTrackbar('width', 'tracking',0,width,w1)
# cv2.createTrackbar(switch,'hasbullah',0,1,nothing)


while True:
    blue = img[w, h, 0]
    green = img[w, h, 1]
    red = img[w, h, 2]
    clr = np.zeros((200,200,3),np.uint8)
    clr[:] = img[h, w]
    font = cv2.FONT_HERSHEY_PLAIN
    text = "[b =" + str(blue) + "g= " + str(green) + "r= " + str(red) + "]"
    cv2.putText(clr, text, (25, 100), font, 1, (255 - int(blue), 255 - int(green), 255 - int(red)), 1,cv2.LINE_AA)
    cv2.imshow('color', clr)
    cv2.imshow('hasbullah',img)
    k = cv2.waitKey(1)

    h = cv2.getTrackbarPos('height', 'tracking')
    w = cv2.getTrackbarPos('width', 'tracking')

    clr[:] = img[w, h]
    # print("bgr : b =" + str(blue) + "g= " + str(green) + "r= " + str(red))

    # print(str(h) + " " + str(w))

    if k == ord('q'):
        break







cv2.destroyAllWindows()
