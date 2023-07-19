import cv2
from matplotlib import pyplot as plt
import numpy as np
def nothing(x):
    pass

cv2.namedWindow('thresholds')
cv2.createTrackbar('threshold 1', 'thresholds', 0, 255, nothing)
cv2.createTrackbar('threshold 2', 'thresholds',0, 255, nothing)
img = cv2.imread("images/sudoku.PNG", 0)
canny = cv2.Canny(img, 0, 0)
while True:
    cv2.imshow('frame', canny)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    th1 = cv2.getTrackbarPos('threshold 1', 'thresholds')
    th2 = cv2.getTrackbarPos('threshold 2', 'thresholds')
    canny = cv2.Canny(img, th1, th2)
cv2.destroyAllWindows()


lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
sobelX = np.uint8(np.absolute(sobelX))
sobelCombined = cv2.bitwise_or(sobelY,sobelX)


titles = ['image', 'laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(3,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
