cat << 'EOF' > README.md
# License Tracker

A web application for automatic license plate detection and recognition using YOLO, AWS S3 for image storage, and AWS Textract for text extraction. The app is built with Streamlit and deployed on an AWS EC2 instance.

---

## Features

- Upload vehicle images to detect license plates using the YOLO object detection model.
- Save uploaded images and detection results securely in an AWS S3 bucket.
- Extract text from detected license plates using AWS Textract for accurate OCR.
- Interactive web interface powered by Streamlit for easy use.

---

## Tech Stack

- **YOLO** — Real-time object detection for license plates.
- **Streamlit** — Web app framework for Python.
- **AWS S3** — Cloud storage for uploaded images and results.
- **AWS Textract** — OCR service to extract text from license plates.
- **AWS EC2** — Hosting and deployment server.
- **Python 3.12** — Core programming language.
- Other libraries: `boto3`, `opencv-python`, `python-dotenv`, `ultralytics`.

---

## Getting Started

### Prerequisites

- Python 3.12
- AWS account with proper IAM permissions for S3 and Textract.
- AWS CLI configured with credentials.
- YOLO model weights (`best.pt`).

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/license-tracker.git
   cd license-tracker
