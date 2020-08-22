#Read Webcam 

import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)   # Reads vedio from webcaam , 0 denotes the default webcam
cap.set(3, frameWidth)      # width as 3
cap.set(4, frameHeight)     # height as 4
cap.set(10, 100)            # brightness as 10

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):   # If q is pressed the vedio will end
        break
