import cv2
import numpy as np
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        text = 'coordinates: x = ' + str(x) + ' y = ' + str(y)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, text, (x, y), font,1, (0,0,255) ,2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y,x,0]
        red = img[y,x,2]
        green = img[y,x,1]
        text = '[' + str(blue) + ', ' + str(green) + ', ' + str(red) + ']'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, text, (x, y), font, 1, (255-int(blue), 255-int(green), 255-int(red)), 2)
        cv2.imshow('image', img)
        color_img = np.zeros((512,512,3),np.uint8)
        color_img[:] =  [blue, green, red]
        cv2.imshow('color', color_img)

img = cv2.imread('images/hasbullah.PNG', 1)
b,g,r = cv2.split(img)
print(b)
belt = img[476:604, 237:534]
img[56:184,232:529] = belt
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
key = cv2.waitKey(0)
if (key == ord('q')):
    cv2.destroyAllWindows()