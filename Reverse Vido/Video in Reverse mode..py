import cv2

cap = cv2.VideoCapture(r"C:\Users\yaswa\Downloads\sample-10s.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (800, 500))
    frames.append(frame)

cap.release()

for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
