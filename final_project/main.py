import os
import cv2
from flask import Flask, Response, render_template

# 設置環境變數
os.environ["QT_QPA_PLATFORM"] = "xcb"

app = Flask(__name__)

# 開啟USB攝影機（根據需要調整設備索引）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝影機")
    exit()


def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
            )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
