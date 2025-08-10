from dotenv import load_dotenv
import boto3
import cv2
import os
from datetime import datetime
from PIL import Image
import io
load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("REGION_NAME")


textract_client = boto3.client("textract",
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            region_name=region)


s3_client = boto3.client("s3",
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name=region)


def ocr_extraction(image):
    #get & return the text from the cropped license plate
    success, encoded_image = cv2.imencode('.jpg', image)
    if success:
        image_bytes = encoded_image.tobytes()
    else:
        raise ValueError("Could not encode image.")
    response = textract_client.detect_document_text(
        Document = {'Bytes': image_bytes}
    )

    final_result = ""
    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            final_result += block["Text"]
    return final_result

def save_image_s3(res_plotted, plate_number):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    full_image_pil = Image.fromarray(cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB))
    buffer = io.BytesIO()
    full_image_pil.save(buffer, format="JPEG")
    buffer.seek(0)
    key = f"detections/{plate_number}_{timestamp}.jpg"
    s3_client.upload_fileobj(buffer, "licensetrackerbucket", key)
    presigned_url = s3_client.generate_presigned_url(
        'get_object', Params = {'Bucket': 'licensetrackerbucket', 'Key':key}, ExpiresIn=3600
    )
    return presigned_url
