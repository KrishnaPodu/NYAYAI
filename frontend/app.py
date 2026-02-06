import streamlit as st
import base64
import fitz  # PyMuPDF
from PIL import Image
import io

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="NyayAI Document Proofreading",
    layout="wide"
)

st.title("📄 NyayAI Document Proofreading Demo")
st.write(
    "Upload a PDF or Text file to view the original document side-by-side "
    "with the processed/proofread version."
)

# -------------------------------
# Helper: Convert PDF Pages to Images
# -------------------------------
def pdf_to_images(uploaded_file):
    """
    Converts each PDF page into an image for display.
    Returns list of PIL images.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    images = []

    for page in doc:
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)

    return images


# -------------------------------
# Helper: Extract Text from PDF
# -------------------------------
def extract_text_from_pdf(uploaded_file):
    """
    Extracts raw text from PDF pages (basic extraction).
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""

    for page in doc:
        full_text += page.get_text() + "\n"

    return full_text


# -------------------------------
# Dummy Proofreading + Highlighting
# -------------------------------
def highlight_mistakes(text):
    """
    Dummy proofreading example:
    Highlights common spelling mistakes.
    """
    mistakes = {
        "teh": "the",
        "recieve": "receive",
        "adress": "address",
    }

    processed = text

    for wrong, correct in mistakes.items():
        processed = processed.replace(
            wrong,
            f"<span style='background-color:yellow; font-weight:bold;'>{wrong}</span>"
        )

    return processed


# -------------------------------
# Upload Interface
# -------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload a PDF or Text file",
    type=["pdf", "txt"]
)

if uploaded_file:

    # Two-column layout
    col1, col2 = st.columns(2)

    # -------------------------------
    # Case 1: PDF Upload
    # -------------------------------
    if uploaded_file.name.endswith(".pdf"):

        # IMPORTANT:
        # Streamlit reads file only once, so store bytes
        pdf_bytes = uploaded_file.getvalue()

        # Convert pages to images (Original Viewer)
        images = pdf_to_images(io.BytesIO(pdf_bytes))

        # Extract text (for processed output)
        original_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))

        # Process + highlight
        processed_html = highlight_mistakes(original_text)

        # -------------------------------
        # Left Column: Original PDF Viewer
        # -------------------------------
        with col1:
            st.subheader("📌 Original Document (PDF View)")

            if len(images) > 1:
                page_num = st.slider("Select Page", 1, len(images), 1)
            else:
                page_num = 1

            # Select page image
            img = images[page_num - 1]
            img.thumbnail((1200, 1600))

            # Convert image to bytes
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            img_bytes = buf.getvalue()

            # Display inside fixed scroll box with NO top padding
            st.markdown(
                f"""
                <div style="
                    height:600px;
                    overflow-y:scroll;
                    border:1px solid #444;
                    border-radius:10px;
                    background-color:#111;
                    padding:0px;
                    margin:0px;
                ">
                    <img src="data:image/png;base64,{base64.b64encode(img_bytes).decode()}"
                        style="width:100%; display:block; margin:0; padding:0;" />
                </div>
                """,
                unsafe_allow_html=True
            )



        # -------------------------------
        # Right Column: Processed Output
        # -------------------------------
        with col2:
            st.subheader("✅ Processed Document (Proofread View)")

            st.markdown(
                f"""
                <div style="
                    height:650px;
                    overflow-y:scroll;
                    border:1px solid #ccc;
                    border-radius:10px;
                    background-color:#fdfdfd;
                    padding:40px;
                    margin:0;
                    font-size:16px;
                    line-height:1.7;
                    font-family: 'Times New Roman', serif;
                    color:black;
                    box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
                ">
                {processed_html.replace("\n","<br>")}
                </div>
                """,
                unsafe_allow_html=True
            )

    # -------------------------------
    # Case 2: Text File Upload
    # -------------------------------
    else:
        original_text = uploaded_file.read().decode("utf-8")
        processed_html = highlight_mistakes(original_text)

        with col1:
            st.subheader("📌 Original Text File")
            st.text_area("", original_text, height=600)

        with col2:
            st.subheader("✅ Processed Text (Highlighted)")
            st.markdown(
                processed_html,
                unsafe_allow_html=True
            )

else:
    st.info("👆 Please upload a PDF or Text file to begin.")
