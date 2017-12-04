#define your filter
import cv2
import numpy as np
from scipy import ndimage
kenerl_3x3=np.array([[-1,-1,-1],
                     [-1,9,-1],
                     [-1,-1,-1]])
img=cv2.imread("../003.jpg")
f1=cv2.filter2D(img,-1,kenerl_3x3)
f2=cv2.filter2D(f1,-1,kenerl_3x3)
f3=cv2.filter2D(f2,-1,kenerl_3x3)
f4=cv2.filter2D(f3,-1,kenerl_3x3)

cv2.imshow('f1',f1)
cv2.imshow('f2',f2)
cv2.imshow('f3',f3)
cv2.imshow('f4',f4)


cv2.waitKey()
cv2.destroyAllWindows()