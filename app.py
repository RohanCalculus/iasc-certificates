import streamlit as st
from utils.pdf_utils import split_pdf
from utils.zip_utils import zip_pdfs
from utils.bg_utils import set_background, choose_image

# Store the background image in session state
if "bg_url" not in st.session_state:
    st.session_state.bg_url = choose_image()

# Set Background
set_background(st.session_state.bg_url)

# App Header
st.markdown("<h1 style='text-align: left; color: mint;'>IASC Certificate Splitter</h1>", unsafe_allow_html=True)
st.text("")

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
