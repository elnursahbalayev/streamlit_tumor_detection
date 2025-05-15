from ultralytics import YOLO


model = YOLO('yolo12s.pt')


if __name__ == '__main__':
    results = model.train(
        data='Axial-Dataset.v1i.yolov8/data.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        name='my_custom_yolo_training'
    )

    print("Training complete. Model saved to:", results.save_dir)