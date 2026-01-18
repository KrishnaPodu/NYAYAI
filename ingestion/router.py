
import pdfplumber
from ingestion.pdf_text import extract_text_pdf
from ingestion.pdf_scanned import extract_scanned_pdf
from ingestion.tables import extract_tables
from ingestion.maps import extract_maps

def extract_pdf(path):
    with pdfplumber.open(path) as pdf:
        sample = pdf.pages[0].extract_text()

    if sample and len(sample.strip()) > 50:
        return extract_text_pdf(path)
    else:
        return extract_scanned_pdf(path)

def extract_all(pdf_path):
    """Extract text, tables, and maps from PDF"""
    text = extract_pdf(pdf_path)
    extract_tables(pdf_path)
    extract_maps(pdf_path)
    return text

