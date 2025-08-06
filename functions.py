from dotenv import load_dotenv
import boto3
import cv2
import os

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("REGION_NAME")


textract_client = boto3.client("textract",
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
