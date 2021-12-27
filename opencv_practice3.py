import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile('apple.jpg'))
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()