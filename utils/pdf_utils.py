from io import BytesIO
import PyPDF2

def extract_name_from_page(text):
    """
    Extract the recipient's name from the page.
    """
    lines = text.split("\n")
    return lines[-13].strip() if len(lines) > 13 else f"certificate_page_{len(lines)}"

def split_pdf(uploaded_file):
    """
    Splits a multi-page PDF into separate in-memory PDF files.
    """
    reader = PyPDF2.PdfReader(uploaded_file)
    pdf_files = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        name = extract_name_from_page(text)

        writer = PyPDF2.PdfWriter()
        writer.add_page(page)

        pdf_buffer = BytesIO()
        writer.write(pdf_buffer)
        pdf_buffer.seek(0)

        pdf_files.append((f"{name}.pdf", pdf_buffer))

    return pdf_files
