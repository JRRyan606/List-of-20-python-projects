from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Define the PDF template settings
page_width, page_height = letter
margin = 50


# Create a custom PageTemplate with a Frame
def create_page_template(doc):
    frame = Frame(margin, margin, page_width - 2 * margin, page_height - 2 * margin)
    template = PageTemplate(id='default', frames=[frame])
    doc.addPageTemplates([template])
    create_pdf_content(frame)


# Create the content of the PDF
def create_pdf_content(frame):
    styles = getSampleStyleSheet()
    content = []

    # Add paragraphs with content to the PDF
    content.append(Paragraph("Page 1 Content", styles['Normal']))
    content.append(Paragraph("Page 2 Content", styles['Normal']))

    frame.addFromList(content, frame.canvas)


# Generate the PDF template
def generate_pdf_template(filename):
    doc = BaseDocTemplate(filename, pagesize=(page_width, page_height))
    create_page_template(doc)
    doc.build()


if __name__ == '__main__':
    pdf_filename = 'pdf_template.pdf'
    generate_pdf_template(pdf_filename)
    print(f"PDF template generated: {pdf_filename}")
