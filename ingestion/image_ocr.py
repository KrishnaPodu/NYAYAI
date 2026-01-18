```python
from PIL import Image
import pytesseract

def extract_image_text(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)

```