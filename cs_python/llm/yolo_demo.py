from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model(0, show=True)
