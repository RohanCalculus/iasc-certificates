import zipfile
from io import BytesIO

def zip_pdfs(pdf_files):
    """
    Creates a ZIP archive of the split PDF files in memory.
    """
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file_name, pdf_buffer in pdf_files:
            zip_file.writestr(file_name, pdf_buffer.getvalue())

    zip_buffer.seek(0)
    return zip_buffer
