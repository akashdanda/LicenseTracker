from ultralytics import YOLO
import streamlit as st
import os
from PIL import Image
import cv2
import torch
from functions import ocr_extraction, save_image_s3
import numpy as np
UPLOAD_DIR = "uploaded_images_test"

st.title("License Plate Detection")

with st.form(key="license"):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button("Upload")

    if submit_button:
        if uploaded_file is None:
            st.warning("Please upload a file before submitting.")
        else:
            model = YOLO("best.pt")
            image_bytes = uploaded_file.read()
            np_arr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            results = model(image)
            
            #plot image on streamlit
            res_plotted = results[0].plot()
            st.image(res_plotted, caption="Detection Result", use_container_width=True)
 
            #get the coordinates    
            plate_coord = results[0].boxes.data.tolist()
            coord = [plate_coord[0][0], plate_coord[0][1], plate_coord[0][2], plate_coord[0][3]]
            x1, y1, x2, y2 = map(int,coord)


            #license cropped
            plate_img = image[y1:y2, x1:x2]
            plate_img_rgb = cv2.cvtColor(plate_img, cv2.COLOR_BGR2RGB) #to display on streamlit
            st.image(plate_img_rgb)

            #ocr extraction
            license_number = ocr_extraction(plate_img)
            st.write("License Tracker: ",license_number)

            presigned_url = save_image_s3(res_plotted, license_number)
            st.write("View Detection Image Link: ", presigned_url)
