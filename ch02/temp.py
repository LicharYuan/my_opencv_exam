# this is draft

import cv2
import numpy as np

img=cv2.imread('../003.jpg',0)
img=cv2.circle(img,(0,0),100,(255,0,0),1)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()