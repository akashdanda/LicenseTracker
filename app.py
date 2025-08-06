from ultralytics import YOLO
import streamlit as st
import os
from PIL import Image
import cv2

UPLOAD_DIR = "uploaded_images"

st.title("License Plate Detection")

with st.form(key="license"):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button("Upload")

    if submit_button:
        if uploaded_file is None:
            st.warning("Please upload a file before submitting.")
        else:
            if not os.path.exists(UPLOAD_DIR):
                os.makedirs(UPLOAD_DIR)

            file_name = uploaded_file.name
            save_path = os.path.join(UPLOAD_DIR, file_name)

            if os.path.exists(save_path):
                st.error(f"A file named '{file_name}' already exists.")
            else:
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"File '{file_name}' uploaded and saved successfully.")

                # Run inference after saving
                model = YOLO("best.pt")
                results = model(save_path)

                # Get image with detections plotted (numpy array)
                res_plotted = results[0].plot()

                # Show result image in Streamlit
                st.image(res_plotted, caption="Detection Result", use_column_width=True)
