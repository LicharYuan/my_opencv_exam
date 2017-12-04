#HPF(High boost filter)
#A way to detect the edge
import cv2
import numpy as np
from scipy import ndimage
kenerl_3x3=np.array([[-1,-1,-1],
                     [-1,8,-1],
                     [-1,-1,-1]])
kenerl_5x5=np.array([[-1,-1,-1,-1,-1],
                     [-1,1,2,1,-1],
                     [-1,2,4,2,-1],
                     [-1,1,2,1,-1],
                     [-1,-1,-1,-1,-1]])
img=cv2.imread("../003.jpg")
b,g,r=cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
k3=ndimage.convolve(r,kenerl_3x3)
k5=ndimage.convolve(r,kenerl_5x5)
blurred=cv2.GaussianBlur(r,(11,11),0)
cv2.imshow('blurred',blurred)
g_hpf=r-blurred
cv2.imshow('merge',cv2.merge([g,r,g_hpf]))
cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()