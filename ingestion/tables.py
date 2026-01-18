import camelot
import os

def extract_tables(pdf_path, output_dir="data/processed/tables"):
    os.makedirs(output_dir, exist_ok=True)
    tables = camelot.read_pdf(pdf_path, pages="all")

    for i, table in enumerate(tables):
        table.to_csv(f"{output_dir}/table_{i}.csv")
