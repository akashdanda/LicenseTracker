# License Tracker

A web application for automatic license plate detection and recognition using YOLO, AWS S3 for image storage, and AWS Textract for text extraction. The app is built with Streamlit and deployed on an AWS EC2 instance.

## 🚀 Features

- **Automatic License Plate Detection**: Upload vehicle images to detect license plates using the YOLO object detection model
- **Cloud Storage**: Save uploaded images and detection results securely in an AWS S3 bucket
- **OCR Text Extraction**: Extract text from detected license plates using AWS Textract for accurate OCR
- **Interactive Web Interface**: User-friendly interface powered by Streamlit for easy use
- **Real-time Processing**: Fast detection and recognition with visual feedback

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **YOLO** | Real-time object detection for license plates |
| **Streamlit** | Web app framework for Python |
| **AWS S3** | Cloud storage for uploaded images and results |
| **AWS Textract** | OCR service to extract text from license plates |
| **AWS EC2** | Hosting and deployment server |
| **Python 3.12** | Core programming language |

**Additional Libraries**: `boto3`, `opencv-python`, `python-dotenv`, `ultralytics`

## 📋 Prerequisites

Before you begin, ensure you have the following:

- Python 3.12 installed
- AWS account with proper IAM permissions for S3 and Textract
- AWS CLI configured with credentials
- YOLO model weights (`best.pt`)
- Git installed on your system

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/license-tracker.git
cd license-tracker
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials

```bash
aws configure
```

You'll need to provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (e.g., `us-east-1`)
- Default output format (e.g., `json`)

### 5. Environment Variables

Create a `.env` file in the project root (if applicable):

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
S3_BUCKET_NAME=your-bucket-name
AWS_REGION=your-region
```

## 🚦 Running the App

### Local Development

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Open your browser and navigate to `http://localhost:8501`

## ☁️ AWS EC2 Deployment

### Step 1: Launch EC2 Instance

1. Launch an EC2 instance (recommended: `t3.micro` or `t2.micro`)
2. Choose Ubuntu Server as the operating system
3. Configure security groups to allow SSH (port 22) and HTTP traffic (port 8501)
4. Create or use an existing key pair for SSH access

### Step 2: Elastic IP (Optional but Recommended)

1. Allocate an Elastic IP address
2. Associate it with your EC2 instance for a static public IP

### Step 3: Connect and Setup

```bash
# SSH into your instance
ssh -i your-key.pem ubuntu@your-elastic-ip

# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.12 and pip
sudo apt install python3.12 python3.12-venv python3-pip -y

# Install system dependencies
sudo apt install libgl1-mesa-glx -y
```

### Step 4: Deploy Application

```bash
# Clone repository
git clone https://github.com/yourusername/license-tracker.git
cd license-tracker

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure AWS CLI
aws configure

# Run the application
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

### Step 5: Access Your Application

Visit `http://your-elastic-ip:8501` in your browser

## 🔒 Security Group Configuration

Ensure your EC2 security group allows:

| Type | Protocol | Port Range | Source |
|------|----------|------------|---------|
| SSH | TCP | 22 | Your IP/0.0.0.0/0 |
| HTTP | TCP | 8501 | 0.0.0.0/0 |

## 🐛 Troubleshooting

### Common Issues and Solutions

**Issue**: `libGL.so.1: cannot open shared object file`
```bash
sudo apt install libgl1-mesa-glx
```

**Issue**: Connection refused when accessing the app
- Verify Streamlit is running with `--server.address 0.0.0.0`
- Check security groups allow inbound traffic on port 8501
- Ensure the EC2 instance is running

**Issue**: S3 Access Denied
- Verify IAM user has proper S3 and Textract permissions
- Check bucket policies and ACLs
- Ensure AWS credentials are correctly configured

**Issue**: Missing Python modules
```bash
pip install python-dotenv ultralytics opencv-python boto3
```

**Issue**: YOLO model not found
- Ensure `best.pt` file is in the correct directory
- Check file permissions and paths

## 📊 Usage

1. **Upload Image**: Click "Choose an image..." to upload a vehicle photo
2. **Detection**: The app automatically detects license plates using YOLO
3. **OCR Processing**: Detected plates are processed through AWS Textract
4. **Results**: View the extracted text and bounding boxes on the image
5. **Storage**: Images and results are saved to your configured S3 bucket
