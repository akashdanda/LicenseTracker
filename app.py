from ultralytics import YOLO
import streamlit as st
import os
from PIL import Image
import cv2
import torch
from functions import ocr_extraction

UPLOAD_DIR = "uploaded_images_test"

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

                # Get image with detections plotted 
                res_plotted = results[0].plot()
                plate_coord = results[0].boxes.data
                python_list = plate_coord.tolist()
                coord = [python_list[0][0], python_list[0][1], python_list[0][2], python_list[0][3]]
                x1, y1, x2, y2 = map(int,coord)
                st.image(res_plotted, caption="Detection Result", use_container_width=True)
                image = cv2.imread(save_path)
                plate_img = image[y1:y2, x1:x2]
                plate_img_rgb = cv2.cvtColor(plate_img, cv2.COLOR_BGR2RGB) #to display on streamlit
                st.image(plate_img_rgb)
                st.write("License Tracker: ",ocr_extraction(plate_img))
