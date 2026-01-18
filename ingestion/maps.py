import fitz  # PyMuPDF
import os

def extract_maps(pdf_path, output_dir="data/processed/maps"):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)

    for pno, page in enumerate(doc):
        for idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            pix.save(f"{output_dir}/map_{pno}_{idx}.png")
