import cv2

cap = cv2.VideoCapture(0)  # 嘗試其他索引如1，2等

if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法獲取影像")
        break

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
