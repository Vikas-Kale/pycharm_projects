# how to create image using numpy zeroe's method

import numpy as np
import cv2

img = np.zeros([512, 512, 3], np.uint8)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Vikas', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
