import cv2
import numpy as np

img = cv2.imread('images/sudoku.PNG')
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imGray,26,58, apertureSize=3)

# region HoughLines
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)
# endregion

# region HoughLinesP
linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 100,  minLineLength=50, maxLineGap=10)
for line in linesP:
    x1,y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0),2)
# endregion
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()