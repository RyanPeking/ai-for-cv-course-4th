import cv2
import numpy as np

img = cv2.imread('lenna.jpg')
print(img)
cv2.imshow('lenna', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

# # # Gaussian Kernel Effect
# g_img = cv2.GaussianBlur(img,(7,7),1)
# cv2.imshow('gaussian_blur_lenna', g_img)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()
#
# g_img = cv2.GaussianBlur(img, (7, 7), 5)
# cv2.imshow('gaussian_blur_lenna', g_img)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()


# 2nd derivative: laplacian （双边缘效果）
kernel_lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_lap)
print(lap_img)
cv2.imshow('lap_lenna', lap_img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

# 应用： 图像锐化 = edge+ori
# app: sharpen
# 图像+edge=更锐利地图像，因为突出边缘
kernel_sharp = np.array([[0, 1, 0], [1, -3, 1], [0, 1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('sharp_lenna', lap_img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

# 这样不对，因为，周围有4个1，中间是-3，虽然有边缘效果，但是周围得1会使得原kernel有滤波效果，使图像模糊；
# 解决：所以取kernel_lap得相反数，再加上原图像，这样突出了中心像素，效果类似于小方差的高斯，所以
#      可以既有边缘效果，又保留图像清晰度
kernel_sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('sharp_lenna', lap_img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
#

# img = cv2.imread('lenna.jpg')
# # create sift class
# sift = cv2.xfeatures2d.SIFT_create()
# # detect SIFT
# kp = sift.detect(img,None)   # None for mask
# # compute SIFT descriptor
# kp,des = sift.compute(img,kp)
# print(des.shape)
# img_sift= cv2.drawKeypoints(img,kp,outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow('lenna_sift.jpg', img_sift)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()