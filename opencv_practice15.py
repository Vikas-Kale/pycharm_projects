import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255,255,255), -1)
img2 = cv2.imread('image1.jpg')
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))
print(img1.shape)
print(img2.shape)

# bitAND = cv2.bitwise_and(img2, img1)  # AND operator
# bitOR = cv2.bitwise_or(img2, img1)  # OR operator
# bitXOR = cv2.bitwise_xor(img2, img1)  # XOR operator
bitNOT1 = cv2.bitwise_not(img1)
bitNOT2 = cv2.bitwise_not(img2)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
# cv2.imshow('bitXOR', bitXOR)
cv2.imshow('bitNOT1', bitNOT1)
cv2.imshow('bitNOT2', bitNOT2)

cv2.waitKey(0)
cv2.destroyAllWindows()