# Color detection
import cv2
import numpy as np


def empty():
    pass


path = 'Resources/charizard.png'

# For Testing and to find the value
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240) # size of the window
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("sat Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("val Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)

# after finding the values change the values for the final mask and comment the default range given to check

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)  # size of the window
cv2.createTrackbar("Hue Min", "TrackBars", 1, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 82, 179, empty)
cv2.createTrackbar("sat Min", "TrackBars", 93, 255, empty)
cv2.createTrackbar("sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)  # as result found in the trackbar (10, 13, 96, 253, 0, 255)


while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imageResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original image', img)
    cv2.imshow('HSV image', imgHSV)
    cv2.imshow('masked image', mask)
    cv2.imshow('Result', imageResult)

    cv2.waitKey(1)
