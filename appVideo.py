import streamlit as st
import pandas as pd
import qrcode
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from PIL import Image
import datetime
import time
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Dashboard", layout ="wide")

st.write("webRTC")  
