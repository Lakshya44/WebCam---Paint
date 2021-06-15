import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("trackbar")
cv2.createTrackbar("L-H", "trackbar", 0, 179, nothing)
cv2.createTrackbar("L-S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("L-V", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U-H", "trackbar", 179, 179, nothing)
cv2.createTrackbar("U-S", "trackbar", 255, 255, nothing)
cv2.createTrackbar("U-V", "trackbar", 255, 255, nothing)

cam = cv2.VideoCapture(0)

while cam.isOpened():

    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "trackbar")
    l_s = cv2.getTrackbarPos("L-S", "trackbar")
    l_v = cv2.getTrackbarPos("L-V", "trackbar")
    h_h = cv2.getTrackbarPos("U-H", "trackbar")
    h_s = cv2.getTrackbarPos("U-S", "trackbar")
    h_v = cv2.getTrackbarPos("U-V", "trackbar")

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([h_h, h_s, h_v])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("result", result)

    if cv2.waitKey(1) == ord('s'):
        arr = [[l_h, l_s, l_v], [h_h, h_s, h_v]]
        np.save('pen', arr)
        break
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
