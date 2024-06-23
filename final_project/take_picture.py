import cv2

def take_picture():
    # 使用cv2.VideoCapture(0)來設置攝像頭
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    # 從攝像頭中讀取畫面
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        return

    # 將畫面儲存為圖片
    cv2.imwrite('photo.jpg', frame)

    # 釋放攝像頭資源
    cap.release()
    cv2.destroyAllWindows()

    print("Picture taken and saved as photo.jpg")

# 呼叫拍照函數
take_picture()
