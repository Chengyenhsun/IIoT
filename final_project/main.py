from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# 打開USB攝像頭
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def gen_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            # 將每一幀影像轉換成byte格式
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # 產生影像的generator

@app.route('/')
def index():
    return render_template('index.html')  # 渲染index.html模板

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
