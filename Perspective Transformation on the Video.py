import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\yaswa\Downloads\sample-10s.mp4")

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    h, w = frame.shape[:2]

    # Source points
    pts1 = np.float32([[100,100], [w-100,100], [100,h-100], [w-100,h-100]])

    # Destination points
    pts2 = np.float32([[0,0], [w,0], [0,h], [w,h]])

    # Perspective matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    result = cv2.warpPerspective(frame, matrix, (w, h))

    # Resize output frame to fixed size (example: 640x480)
    result = cv2.resize(result, (640, 480))

    cv2.imshow("Perspective Video", result)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
