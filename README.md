# Brain MRI Tumor Detection

## Overview
This application uses deep learning to detect tumors in brain MRI scans. It provides a user-friendly web interface built with Streamlit where users can upload MRI images and get instant tumor detection results.

## Features
- Upload brain MRI images in common formats (PNG, JPG, JPEG)
- Real-time tumor detection using a custom-trained YOLO model
- Interactive visualization with options to view original and annotated images
- User-friendly interface with custom background

## Technologies Used
- **Streamlit**: For the web application interface
- **YOLO (You Only Look Once)**: For object detection
- **Ultralytics**: Implementation of YOLOv8
- **PyTorch**: Deep learning framework
- **Plotly**: For interactive visualizations
- **OpenCV & Pillow**: For image processing

## Installation

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended for faster inference)

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/streamlit_tumor_detection.git
   cd streamlit_tumor_detection
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Unix or MacOS
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run main.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Upload a brain MRI image using the file uploader

4. View the detection results - you can toggle between the original image and the image with tumor detections

## Model Training

The tumor detection model was trained using a YOLOv8 architecture on a custom dataset of brain MRI scans. To retrain the model:

1. Prepare your dataset in YOLOv8 format
2. Run the training script:
   ```
   python train_yolo.py
   ```

Training parameters can be adjusted in the `train_yolo.py` file.

## Dataset

The model was trained on the Axial-Dataset, which contains annotated brain MRI scans with tumor regions marked.

## License

[Add your license information here]

## Acknowledgements

- [Add any acknowledgements here]
