```python
from pdf2image import convert_from_path
import pytesseract

def extract_scanned_pdf(path):
    images = convert_from_path(path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"
    return text

```