import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
cv2.imshow('img',img)
ret, thresh = cv2.threshold(img, 127, 255, 0)
cv2.imshow('ret',ret)
cv2.imshow('thresh',thresh)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#This function need the images type as binary
#findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> image, contours, hierarchy
#mode:cv2.RETR_TREE: bulid a contours of structure of hierarchy tree
#     cv2.RETR_EXTERNAL :only detect outer boarder
#     cv2.RETR_LIST: detect the contours without build the hierarchy
#     cv2.RETR_CCOMP:build the contours of two hierarchy
#     cv2.CHAIN_APPROX_NONE:save all contour points,the diff position of two adjacent pixels less than 1
# cv2.CHAIN_APPROX_SIMPLE,cv2.CHAIN_APPROX_SIMPLE,cv2.CHAIN_APPROX_TC89_KCOS,cv2.CHAIN_APPROX_TC89_L1

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
