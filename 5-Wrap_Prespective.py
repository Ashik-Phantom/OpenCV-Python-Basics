# Warp Perspective
# To wrap a specific part from a image

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
resize = cv2.resize(img, (500, 500))

width, height = 500, 500
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])  # get points of the part from paint or any software
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", imgOutput)
cv2.imshow("Card", resize)

cv2.waitKey(0)
