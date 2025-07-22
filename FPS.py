import cv2
import time

cap = cv2.VideoCapture(1)  # 또는 '/dev/video0' 등

if not cap.isOpened():
    print("카메라 열기 실패")
    exit()

# FPS 측정
frame_count = 0
start_time = time.time()

while frame_count < 100:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1

end_time = time.time()
elapsed = end_time - start_time
fps = frame_count / elapsed
print(f"FPS: {fps:.2f}")

cap.release()