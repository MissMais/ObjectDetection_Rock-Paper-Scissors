from ultralytics import YOLO

model = YOLO("best.pt")

def predictionFunc(path):
    prediction = model.predict(path, save=True, conf=0.5)
    return prediction
