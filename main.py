import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

from util import visualize, set_background

set_background('./bg.png')

st.title('Brain MRI tumor detection')
st.header('Please upload an image')

file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

predictor = YOLO('runs/detect/my_custom_yolo_training6/weights/best.pt')

if file:
    image = Image.open(file).convert('RGB')
    image_array = np.asarray(image)

    outputs = predictor(image_array)

    threshold = 0.5
    for result in outputs:
        scores = result.probs
        bboxes = result.boxes

        bboxes_ = []
        if bboxes and scores:
            for j, bbox in enumerate(bboxes):

                score = scores[j]

                if score > threshold:
                    x1, y1, x2, y2 = [int(i) for i in bbox]
                    bboxes_.append([x1, y1, x2, y2])

        visualize(image, bboxes_)
