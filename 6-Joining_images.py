# Joining images

import cv2
import numpy as np

img = cv2.imread('Resources/charizard.png')

imghor = np.hstack((img, img))   # Horizontal Join
imgver = np.vstack((img, img))   # Vertical Join

cv2.imshow("horizontal", imghor) 
cv2.imshow("vertical", imgver)

cv2.waitKey(0)

#Note: pictures with different filters cannet be merged , we have to use seperate funtion to merge them which will be available in code 6.1
