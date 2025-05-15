import streamlit as st
from PIL import Image
import numpy as np

from util import visualize, set_background

set_background('./bg.png')

st.title('Brain MRI tumor detection')
st.header('Please upload an image')

file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

predictor = ...

if file:
    image = Image.open(file).convert('RGB')
    image_array = np.asarray(image)

    outputs = predictor(image_array)

    threshold = 0.5

    preds = outputs['instances'].pred_classes.tolist()
    scores = outputs['instances'].scores.tolist()
    bboxes = outputs['instances'].pred_boxes

    bboxes_ = []
    for j, bbox in enumerate(bboxes):
        bbox = bbox.tolist()

        score = scores[j]
        pred = preds[j]

        if score > threshold:
            x1, y1, x2, y2 = [int(i) for i in bbox]
            bboxes_.append([x1, y1, x2, y2])

    visualize(image, bboxes_)