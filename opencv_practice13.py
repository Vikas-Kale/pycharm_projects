# import numpy as np
import cv2

img = cv2.imread('images.jfif', 1)
img = cv2.resize(img, (800,800)) # widthxheight
print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[237:280, 117:160]
img[184:231, 128:149] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()