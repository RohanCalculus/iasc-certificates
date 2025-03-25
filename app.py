import streamlit as st
from utils.pdf_utils import split_pdf
from utils.zip_utils import zip_pdfs
from utils.bg_utils import set_background, choose_image

# Page Configuration
st.set_page_config(
    page_title="IASC Certificate Splitter",
    page_icon="📜"
)

# Store the background image in session state
if "bg_url" not in st.session_state:
    st.session_state.bg_url = choose_image()

# Set Background
set_background(st.session_state.bg_url)

# App Header
st.markdown("<h1 style='text-align: left; color: #f09d0e;'>📜 IASC Certificate Splitter</h1>", unsafe_allow_html=True)
st.text("")

# How to Use the App Box
with st.expander(":red[**How to Use the App?**]", expanded=False):
    st.markdown(
        """
        <div style='background-color: rgba(0, 0, 0, 0.8); padding: 5px; border-radius: 10px; margin: 0px 0px 10px 0px'>
            <ol>
                <li><b>Upload</b> the PDF file containing multiple certificates.</li>
                <li>The application <b>processes</b> the document and extracts each certificate.</li>
                <li>Each certificate is <b>saved individually</b>, named after the recipient.</li>
                <li><b>Download</b> the split certificates for easy distribution.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

# File Uploader
uploaded_file = st.file_uploader("Upload Multi-Page Certificate PDF:", type=["pdf"])

# Process PDF immediately once uploaded
if uploaded_file:
    pdf_files = split_pdf(uploaded_file)
    if pdf_files:
        zip_file = zip_pdfs(pdf_files)
        st.success("PDFs split successfully!")
        st.download_button(
            label="Download Split PDFs as ZIP file",
            data=zip_file,
            file_name="IASC-Certificates.zip",
            mime="application/zip"
        )
    else:
        st.error("Could not extract names. Please check the file format.")
