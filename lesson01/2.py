import cv2
import numpy as np


img1 = cv2.imread("timg.jpg")
print(img1.dtype)
cv2.imshow("1", img1)

img2 = img1+450
print(img2.dtype)
cv2.imshow("2", img2)

img3 = img2.astype(np.uint8)
print(img3.dtype)
cv2.imshow("3", img3)

a = np.array([1, 255, 256, 257], dtype=np.uint8)
print(a)
a = np.array([1, 255, 256, 257], dtype=np.uint16)
print(a)
a1 = a.astype(np.uint8)
print(a1)

img4 = cv2.normalize(img2, None, 0,255, cv2.NORM_MINMAX)

print(img4.dtype)
print(img4==img1)
img4 = img4.astype(np.uint8)
cv2.imshow("4", img4)

img5 = img1+20000
print(img5.dtype)
cv2.imshow("5", img5)

img6 = img1+30000
print(img6.dtype)
cv2.imshow("6", img6)

img7 = img1+40000
print(img7.dtype)
cv2.imshow("7", img7)

img8 = img1+50000
print(img8.dtype)
cv2.imshow("8", img8)

cv2.waitKey(0)