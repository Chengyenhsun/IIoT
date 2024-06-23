from ultralytics import YOLO

model = YOLO("best.pt")

res = model.predict("tcp://127.0.0.1:8888", show=True)
