# Contours / Shape detection
import cv2
import numpy as np


def getContours(img):
    # img is imgCanny
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # -1 to print all shape
            peri = cv2.arcLength(cnt, True)
            print(peri)
            aprox = cv2.approxPolyDP(cnt, 0.02*peri, True)  #True because its a closed image
            print(len(aprox))
            objcor = len(aprox)
            x, y, w, h = cv2.boundingRect(aprox)

            if objcor == 3: objecttype = "Tri"
            elif objcor == 6: objecttype = "pent"
            elif objcor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05: objecttype='Square'
                else: objecttype= "Rectangle"
            elif objcor>6: objecttype = "Circle"
            else: objecttype="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)  # creating boundary boxes
            cv2.putText(imgContour, objecttype,
                        (x+(w//2)-10,y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

path = 'Resources/shapes1.png'
img = cv2.imread(path)
imgContour = img.copy()
# change to gray scale and find the edges
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 2)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

cv2.imshow("original", img)
cv2.imshow("ImageContour", imgContour)

cv2.waitKey(0)
