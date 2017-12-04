#This code is for test
import numpy as np
import cv2
img=np.zeros((3,3),dtype=np.uint8)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#cv2.cvtColor turn the gary to BGR
print(img)

#------------------0-----------------------------

import cv2
grayImage=cv2.imread('/home/lichar/database/test/000.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('/home/lichar/database/test/000_gary.jpg',grayImage)
#read the pic as gray model
#imwrite() ask the the pics as BGR or Gray mode and every channel need certain bits (bmp need 8 bits PNG 8 or 16)
#-------------------1---------------------------------

#a example to change the bytearray contains random bytes into the gray pic and BGR image
import  cv2
import numpy
import os

#make an array of 120,000 random bytes
randomByteArray=bytearray(os.urandom(120000))
flatNumpyArray=numpy.array(randomByteArray)
#Convert the array to make a 400x300 grayscale image
grayImage=flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

#Convert the array to make a 400x100 color image
bgrImage=flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImage)

#----------------3----------------------------

import cv2
import numpy as np
img=cv2.imread('/home/lichar/database/test/000.jpg')

print(img.item(150,120,0))#print the current value of B for that pixel
img.itemset((150,120,0),255)#set the pixel
print(img.item(150,120,0))

#--------------4----------------------------------------
import  cv2
import numpy as np
img=cv2.imread('/home/lichar/database/test/000.jpg')
img[:,:,1]=0
cv2.imwrite('000_NoGreen.jpg',img)
cv2.imshow('000',np.array([0,0,0]))
cv2.waitKey()  #keep the window open
cv2.destroyAllWindows()

# so the imshow just show the pic consisted of your data
# if you want to show your pic ,you must read the data before
#-----------------------------5----------------------------

