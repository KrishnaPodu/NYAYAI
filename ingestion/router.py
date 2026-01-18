```python
import pdfplumber
from ingestion.pdf_text import extract_text_pdf
from ingestion.pdf_scanned import extract_scanned_pdf

def extract_pdf(path):
    with pdfplumber.open(path) as pdf:
        sample = pdf.pages[0].extract_text()

    if sample and len(sample.strip()) > 50:
        return extract_text_pdf(path)
    else:
        return extract_scanned_pdf(path)

```