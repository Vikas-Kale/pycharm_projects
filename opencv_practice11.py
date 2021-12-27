import numpy as np
import cv2


def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = [x, y, 0]
        green = [x, y, 1]
        red = [x, y, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycology = np.zeros((512, 512, 3), np.uint8)

        mycology[:] = [blue, green, red]
        cv2.imshow('color', mycology)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
