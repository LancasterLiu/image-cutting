from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo path")
results = model.predict("image path", save=True, save_txt=True)
