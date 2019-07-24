import random

import cv2
import numpy as np

img_gray_fu1 = cv2.imread('timg.jpg', -1)
img_gray_0 = cv2.imread('timg.jpg', 0)
img_gray_1 = cv2.imread('timg.jpg', 1)
img_gray_2 = cv2.imread('timg.jpg', 2)
img_gray_3 = cv2.imread('timg.jpg', 3)
img_gray_4 = cv2.imread('timg.jpg', 4)
"""flag=-1时，8位深度，原通道
flag=0，8位深度，1通道
flag=1,   8位深度  ，3通道
flag=2，原深度，1通道
flag=3,  原深度，3通道
flag=4，8位深度 ，3通道"""

# imgs = np.hstack([img_gray_fu1, img_gray_0, img_gray_1, img_gray_2, img_gray_3, img_gray_4])

# cv2.imshow('fu1', img_gray_fu1)
# cv2.imshow('0', img_gray_0)
# cv2.imshow('1', img_gray_1)
# cv2.imshow('2', img_gray_2)
# cv2.imshow('3', img_gray_3)
# cv2.imshow('4', img_gray_4)
#
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

# print(img_gray_0)
# print(img_gray_1)
# print(img_gray_0.dtype)
# print(img_gray_0.shape)
#
img = cv2.imread('timg.jpg')
print(img[0])
print("----------------------------")
print(img[0] + 450)
img = img + 450
print(img[0] % 255)
cv2.imshow('450', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
cv2.imshow('book', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
print(img)
print(img.shape)

# img_crop = img[0:100, 0:200]
# cv2.imshow('img_crop', img_crop)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

# B, G, R = cv2.split(img)
# cv2.imshow('B', B)
# cv2.imshow('G', G)
# cv2.imshow('R', R)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

# def random_light_color(img):
#     B, G, R = cv2.split(img)
#
#     b_rand = random.randint(-50, 50)
#     if b_rand == 0:
#         pass
#     elif b_rand > 0:
#         lim = 255 - b_rand
#         B[B > lim] = 255
#         B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)
#     elif b_rand < 0:
#         lim = 0 - b_rand
#         B[B < lim] = 0
#         B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)
#
#     g_rand = random.randint(-50, 50)
#     if g_rand == 0:
#         pass
#     elif g_rand > 0:
#         lim = 255 - g_rand
#         B[B > lim] = 255
#         B[B <= lim] = (g_rand + B[B <= lim]).astype(img.dtype)
#     elif g_rand < 0:
#         lim = 0 - g_rand
#         B[B < lim] = 0
#         B[B >= lim] = (g_rand + B[B >= lim]).astype(img.dtype)
#
#     r_rand = random.randint(-50, 50)
#     if r_rand == 0:
#         pass
#     elif r_rand > 0:
#         lim = 255 - r_rand
#         B[B > lim] = 255
#         B[B <= lim] = (r_rand + B[B <= lim]).astype(img.dtype)
#     elif r_rand < 0:
#         lim = 0 - r_rand
#         B[B < lim] = 0
#         B[B >= lim] = (r_rand + B[B >= lim]).astype(img.dtype)
#
#     img_merge = cv2.merge((B, G, R))
#     return  img_merge
#
# img_random_color = random_light_color(img)
# cv2.imshow('img_random_color', img_random_color)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

# gamma correction
# def adjust_gamma(image, gamma=1.0):
#     invGamma = 1.0/gamma
#     table = []
#     for i in range(256):
#         table.append(((i / 255.0) ** invGamma) * 255)
#     table = np.array(table).astype('uint8')
#     return cv2.LUT(img, table)
#
# img_brighter = adjust_gamma(img, 2)
# cv2.imshow('img_dark', img)
# cv2.imshow('img_brighter', img_brighter)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()