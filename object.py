import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('TrackBar')
cv2.createTrackbar('l_r', 'TrackBar', 0, 179, nothing)
cv2.createTrackbar('l_g', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('l_b', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('u_r', 'TrackBar', 179, 179, nothing)
cv2.createTrackbar('u_g', 'TrackBar', 255, 255, nothing)
cv2.createTrackbar('u_b', 'TrackBar', 255, 255, nothing)
cap = cv2.VideoCapture(0)

while cap.isOpened():

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    try:
        l_r = cv2.getTrackbarPos('l_r', 'TrackBar')
        l_g = cv2.getTrackbarPos('l_g', 'TrackBar')
        l_b = cv2.getTrackbarPos('l_b', 'TrackBar')
        u_r = cv2.getTrackbarPos('u_r', 'TrackBar')
        u_g = cv2.getTrackbarPos('u_g', 'TrackBar')
        u_b = cv2.getTrackbarPos('u_b', 'TrackBar')

        lower = np.array([l_r, l_g, l_r])
        upper = np.array([u_r, u_g, u_b])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('result', result)

        if cv2.waitKey(1) == ord('s'):
            a = [lower, upper]
            np.save('object', a)
            break

        if cv2.waitKey(1) == 27:
            break

    except:
        print('Camera could not be opened')
        break

cap.release()
cv2.destroyAllWindows()
