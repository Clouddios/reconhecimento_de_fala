from docx import Document
from fpdf import FPDF

def save_to_docx(text, file_name):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(f"exports/{file_name}.docx")

def save_to_pdf(text, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(f"exports/{file_name}.pdf")
