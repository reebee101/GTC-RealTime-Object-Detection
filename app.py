import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load your trained model
model = YOLO("runs/train/bdd100k_yolov8n3/weights/best.pt")

st.title("Real-Time Object Detection Demo")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    results = model(img)  # Run inference
    st.image(results[0].plot(), caption="Detected Objects", use_column_width=True)