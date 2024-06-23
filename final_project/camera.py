import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# 初始化YOLO模型
model = YOLO("yolov8n.pt")

# 開啟USB攝影機（通常是設備0，如果有多個攝影機，設備號可能不同）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# 逐幀讀取影像並顯示
while True:
    ret, frame = cap.read()
    if not ret:
        print("無法獲取影像")
        break

    # 使用matplotlib顯示影像
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    # 按q鍵退出
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 釋放攝影機並關閉所有OpenCV窗口
cap.release()
cv2.destroyAllWindows()
