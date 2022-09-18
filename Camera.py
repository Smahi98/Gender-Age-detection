import streamlit as st
from streamlit_webrtc import webrtc_streamer
from predict import read_from_camera

st.markdown("## Face detection")

st.text('Welcome to realtime face, gender and age detection.\n\nClick on start to begin:')

import av


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = read_from_camera(img)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
