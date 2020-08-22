# Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # (h, w, channel)
# print(img)
# img[:] = 0, 255, 0  # BGR

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 5)                   # (img , pt1, pt2, color, thickness)
cv2.rectangle(img, (100,100), (250,350), (0,0,255), cv2.FILLED)                       # (img , pt1, pt2, color, thickness)
cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 50, (0, 255, 255), 4)             # (img , centre, radius, color, thickness)
cv2.putText(img, "OPENCV ", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)   # (img, text, org, fontfamily, fomtsoze, color, thickness)

cv2.imshow("Image", img)  # Img containing all those shapes which are generated

cv2.waitKey(0)
