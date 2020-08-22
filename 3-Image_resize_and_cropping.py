# image resize and cropping

import cv2

img = cv2.imread("Resources/starmine.png")
print(img.shape)  # (h, w, channel(bgr))

imgResize = cv2.resize(img, (300, 200))  # (w, h)
print(imgResize.shape)

imgCropped = img[0:50, 30:256]  # [h(from:to), w(from:to)]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
