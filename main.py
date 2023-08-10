from ultralytics import YOLO

model = YOLO('yolov8s.yaml')
results = model.train(data="ds.yaml", epochs=100)
