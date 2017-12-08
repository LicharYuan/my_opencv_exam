#canny
import cv2
import numpy as np
img=cv2.imread("../003.jpg")
cv2.imwrite('canny.jpg',cv2.Canny(img,100,300))
#canny is very complex
#it contains the following steps:
#1.denosing through Gaussian filter
#2.calculate the gradient
#3.applyong NMS in the edge
#4.Using double threshold to eliminate the false positive in the area detecting the edge
#5.analying the connection between the edges
cv2.imshow('canny',cv2.imread('canny.jpg'))
cv2.waitKey()
cv2.destroyAllWindows()