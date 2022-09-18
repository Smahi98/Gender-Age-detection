import cv2
import streamlit as st

from predict_from_image import read_from_image

st.markdown("## Face detection")

st.text('Welcome, run the models on a specific image')

uploaded_files = st.file_uploader('Upload an image', type=['.jpg', '.png', '.jpeg'], accept_multiple_files=True)

# detect from a camera stream
image = st.button('Detection from image')
if image:
    if uploaded_files == []:
        st.warning('Please select an image first')

    for fs in uploaded_files:
        with open(fs.name, 'wb') as f:
            f.write(fs.read())
        image = cv2.imread(fs.name)
        image = read_from_image(image=image)
        st.image(image, channels='bgr')
