# Face detection - Only detects the face not the person
import cv2

facecascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")   # Pre trained face model
Img = cv2.imread('Resources/my_pic1.jpeg')
img = cv2.resize(Img,(600,600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find faces
faces = facecascade.detectMultiScale(imgGray, 1.1, 10)  # (scale factor, minimum) neighbour change based on results

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Result', img)

cv2.waitKey(0)
