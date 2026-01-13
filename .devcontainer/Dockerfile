FROM python:3.10-slim

# Install System Dependencies
# We use libgl1 instead of libgl1-mesa-glx for modern Debian compatibility
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    poppler-utils \
    git \
    && rm -rf /var/lib/apt/lists/*

# Add Hindi support for Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr-hin \
    tesseract-ocr-eng \
    poppler-utils \
    libgl1 # Required for OpenCV

WORKDIR /workspaces/NyayAI

# Create a dummy requirements file so the build doesn't fail
RUN touch requirements.txt

# Install Python Libraries
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir transformers langchain chromadb easyocr pymupdf opencv-python ultralytics python-dotenv