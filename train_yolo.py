from ultralytics import YOLO


model = YOLO('yolo11s.pt')


if __name__ == '__main__':
    results = model.train(
        data='Axial-Dataset.v1i.yolov8/data.yaml',
        epochs=100,
        imgsz=640,
        batch=32,
        name='my_custom_yolo_training',
        device=0
    )

    print("Training complete. Model saved to:", results.save_dir)