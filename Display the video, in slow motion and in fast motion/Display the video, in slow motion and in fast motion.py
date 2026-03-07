import cv2
import time

cap = cv2.VideoCapture(r"C:\Users\yaswa\Downloads\sample-10s.mp4")

print("s = Slow | f = Fast | n = Normal | q = Quit")

mode = 1   

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 500))
    cv2.imshow("Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        mode = 0.2
    elif key == ord('f'):
        mode = 5
    elif key == ord('n'):
        mode = 1
    elif key == ord('q'):
        break

    # Slow motion
    if mode == 0.2:
        time.sleep(mode)

    # Fast motion
    if mode == 5:
        for _ in range(mode):
            cap.read()

cap.release()
cv2.destroyAllWindows()
