import streamlit as st
import pandas as pd
import qrcode
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Dashboard", layout ="wide")

st.write("webRTC")  

webrtc_streamer(key="example")
