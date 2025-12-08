import streamlit as st
from main import predictionFunc
from PIL import Image
import os


st.title('Detect the class')

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    save_dir = "uploaded_images"
    os.makedirs(save_dir, exist_ok=True)
    file_name = uploaded_file.name
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    img = Image.open(file_path)
    st.image(img, use_container_width=True)

    pred = predictionFunc(file_path)
    one = pred[0].save_dir.split('\\')[-1]
    two = pred[0].save_dir.split('\\')[-2]
    three = pred[0].save_dir.split('\\')[-3]

    st.text('Predicted Label:')
    image = Image.open(f'{three}/{two}/{one}/{file_name}')
    st.image(image, use_container_width=True)
