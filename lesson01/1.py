import random

import cv2
import numpy as np
import matplotlib.pyplot as plt

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
# print(img[0])
# print("----------------------------")
# print(img[0] + 450)
# print("----------------------------")
# print('转化成8位无符号为：\n{}'.format(np.array(img[0] + 450).astype(np.uint8)))
# img = img + 450
# cv2.imshow('450', img)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()
# cv2.imshow('book', img)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()
# print(img)
# print(img.shape)

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
def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0/gamma
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype('uint8')
    return cv2.LUT(img, table)

img_brighter = adjust_gamma(img, 2)
cv2.imshow('img_dark', img)
cv2.imshow('img_brighter', img_brighter)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

# histogram
# img_small_brighter = cv2.resize(img_brighter, (int(img_brighter.shape[0]*0.5), (int(img_brighter.shape[1]*0.5))))
# plt.hist(img_brighter.flatten(), 256, [0, 256], color='r')
# plt.show()
# img_yuv = cv2.cvtColor(img_small_brighter, cv2.COLOR_BGR2YUV)
# # equalize the histogram of the Y channel
# img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])   # only for 1 channel
# # convert the YUV image back to RGB format
# img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)   # y: luminance(明亮度), u&v: 色度饱和度
# cv2.imshow('Color input image', img_small_brighter)
# cv2.imshow('Histogram equalized', img_output)
# key = cv2.waitKey(0)
# if key == 27:
#     exit()

# rotation
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 30, 1) # center, angle, scale
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('rotated lenna', img_rotate)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

print(M)

# scale+rotation+translation = similarity transform
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 30, 0.5) # center, angle, scale
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('rotated lenna', img_rotate)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

print(M)

##############################
# Affine Transform
rows, cols, ch = img.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('affine lenna', dst)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

############################
# perspective transform
def random_warp(img, row, col):
    height, width, channels = img.shape

    # warp:
    random_margin = 60
    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img, M_warp, (width, height))
    return M_warp, img_warp
M_warp, img_warp = random_warp(img, img.shape[0], img.shape[1])
cv2.imshow('lenna_warp', img_warp)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()