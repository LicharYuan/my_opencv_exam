import cv2
filepath='/home/lichar/PycharmProjects/opencv_test/011.jpeg'
def detect(filepath):
    face_cascade=cv2.CascadeClassifier('/home/lichar/PycharmProjects/opencv_test/data/haarcascades/haarcascade_frontalface_default.xml')
    img=cv2.imread(filepath)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    print(faces)
    for (x,y,w,h) in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.namedWindow('Detected')
    cv2.imshow('Detected',img)
    # cv2.imwrite('../pics/detect_5_3_1.jpg',img)

if __name__ == '__main__':
    detect(filepath)
    cv2.waitKey()
    cv2.destroyAllWindows()

