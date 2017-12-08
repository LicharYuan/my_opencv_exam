# find lines and circle(roughly)

import cv2
import numpy as np

img=cv2.imread('../015.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,120)
minLineLength=5
maxLineGap=40
lines=cv2.HoughLinesP(edges,1,np.pi/360,100,minLineLength,maxLineGap)#find lines

#draw the lines in your pic
for i in range(lines.shape[0]):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
blur=cv2.medianBlur(gray,5)
cblur=cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=20,maxRadius=500)
circles=np.uint16(np.around(circles))

for i in circles[0,:]:
    #draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('edge',edges)
cv2.imshow('lines',img)
cv2.waitKey()
cv2.destroyAllWindows()