import cv2
import numpy as np

def strokeEdges(src,dst,blursize=7,edgesize=5):
    if blursize>=3:
        blurredSrc=cv2.medianBlur(src,blursize)
        graySrc=cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize=edgesize)
    cv2.imshow('Laplacian',cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize=edgesize))
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    b, g, r = cv2.split(img)
    # print(channels)
    b = b * normalizedInverseAlpha
    g = g * normalizedInverseAlpha
    r = r * normalizedInverseAlpha
    return cv2.merge([b, g, r],dst)

if __name__ == '__main__':
    img=cv2.imread('../003.jpg')
    stroke=strokeEdges(img,dst=None)
    cv2.imshow('strokeEdge',stroke)
    cv2.waitKey()
    cv2.destroyAllWindows()
