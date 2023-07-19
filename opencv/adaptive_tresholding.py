import cv2
from matplotlib import pyplot as plt

# region normal thresholding
bw = cv2.imread("images/blackwhite.jpg", 0)
_, th1 = cv2.threshold(bw, 127,255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(bw, 127,255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(bw, 127,255, cv2.THRESH_OTSU)
_, th4 = cv2.threshold(bw, 127,255, cv2.THRESH_TRUNC)
_, th5 = cv2.threshold(bw, 127,255, cv2.THRESH_TOZERO)
_, th6 = cv2.threshold(bw, 127,255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'OTSU', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [bw, th1, th2, th3, th4, th5 ,th6]

for i in range(7):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# endregion

# region adaptive thresholding
img = cv2.imread("images/hasbullah.PNG", 0)
ath2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
ath3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)

titles = ['Original Image', 'Mean', 'Gaussian']
images = [img, ath2,ath3]
for i in range(3):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# endregion

cv2.waitKey(0)
cv2.destroyAllWindows()
