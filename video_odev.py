import cv2

cap = cv2.VideoCapture(0)

low_red = (0, 100, 100)
upp_red = (10, 255, 255)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maske = cv2.inRange(hsv, low_red, upp_red)
    res = cv2.bitwise_and(frame, frame, mask=maske)
    cv2.imshow("cerceve", frame)
    cv2.imshow("maske", maske)
    cv2.imshow("sonuc", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()