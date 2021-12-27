# import cv2
#
# img = cv2.imread('lena.jpg', 0)
# cv2.imshow('lena.png', img)
#
# k = cv2.waitKey(0)
#
# if k == 27:
#     cv2.destroyWindow()
#
# elif k == ord('s'):
#     cv2.imwrite('lena_copy1.png', img)
#     cv2.destroyWindow()

import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frames = cap.read()
    cv2.imshow('frame', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



