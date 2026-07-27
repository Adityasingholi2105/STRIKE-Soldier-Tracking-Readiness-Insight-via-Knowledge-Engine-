from fpdf import FPDF
import pandas as pd

def export_to_pdf(dataframe, file_name="export.pdf"):
    """Export a Pandas DataFrame to a PDF file."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Personnel Data Export", ln=True, align='C')
    pdf.ln(10)

    # Table Header
    pdf.set_font("Arial", style="B", size=12)
    for col in dataframe.columns:
        pdf.cell(40, 10, col, border=1, align='C')
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", size=10)
    for _, row in dataframe.iterrows():
        for cell in row:
            pdf.cell(40, 10, str(cell), border=1, align='C')
        pdf.ln()

    pdf.output(file_name)
    return file_name
