import cv2
import numpy as np


def nothing(x):
    pass


object_load = np.load('object.npy')

cap = cv2.VideoCapture(0)

cv2.namedWindow('TrackBar')
cv2.createTrackbar('l_r', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('l_g', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('l_b', 'TrackBar', 0, 255, nothing)


canva, toggle, x, y = None, 1, 0, 0

while True:

    _, frame = cap.read()

    frame = cv2.flip(frame, 1)

    r = cv2.getTrackbarPos('l_r', 'TrackBar')
    g = cv2.getTrackbarPos('l_g', 'TrackBar')
    b = cv2.getTrackbarPos('l_b', 'TrackBar')

    if canva is None:
        canva = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, object_load[0], object_load[1])

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > 100:

        c = max(contours, key=cv2.contourArea)
        x1, y1, w, h = cv2.boundingRect(c)

        if not x and not y:
            x, y = x1, y1
        else:
            if (not r) and (not g) and (not b):
                r, g, b = 255, 0, 0
            canva = cv2.line(canva, (x, y), (x1, y1), [r, g, b]*toggle, 8)
            x, y = x1, y1
    else:
        x, y = 0, 0

    frame = cv2.add(frame, canva)
    cv2.imshow('frame', frame)
    cv2.imshow('canva', canva)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('c'):
        canva = None
        print('hello ', canva)

    elif k == ord('e'):
        toggle = int(not toggle)
        print('bye ', toggle)

    elif k == 27:
        break


cap.release()
cv2.destroyAllWindows()
