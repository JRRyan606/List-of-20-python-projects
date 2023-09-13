import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Function to generate a PDF invoice
def generate_pdf_invoice(data):
    pdf_filename = f"Invoice_{data['Invoice Number']}.pdf"

    # Create a PDF canvas
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Define fonts and styles
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(50, 730, f"Invoice Number: {data['Invoice Number']}")
    c.drawString(50, 710, f"Date: {data['Date']}")
    c.drawString(50, 690, f"Customer: {data['Customer Name']}")

    # Draw a table for invoice items
    table_x = 50
    table_y = 640
    row_height = 20

    # Header row
    c.drawString(table_x, table_y, "Item")
    c.drawString(table_x + 200, table_y, "Quantity")
    c.drawString(table_x + 300, table_y, "Price")
    c.drawString(table_x + 400, table_y, "Total")

    table_y -= 20

    # Invoice items
    items = data['Items'].split('\n')
    quantities = str(data['Quantities'])  # Convert to string
    prices = str(data['Prices'])  # Convert to string

    for item, quantity, price in zip(items, quantities.split('\n'), prices.split('\n')):
        c.drawString(table_x, table_y, item)
        c.drawString(table_x + 200, table_y, quantity)
        c.drawString(table_x + 300, table_y, price)
        total = float(quantity) * float(price)
        c.drawString(table_x + 400, table_y, str(total))
        table_y -= row_height

    # Calculate and display the total
    total = sum(float(quantity) * float(price) for quantity, price in zip(quantities.split('\n'), prices.split('\n')))
    c.drawString(table_x + 300, table_y - 20, f"Total: {total}")

    c.save()


# Main function
def main():
    # Load invoice data from an Excel file (replace 'invoices.xlsx' with your file)
    excel_file = 'Invoices.xlsx'
    df = pd.read_excel(excel_file)

    # Loop through each row in the Excel file and generate a PDF invoice
    for index, row in df.iterrows():
        generate_pdf_invoice(row)


if __name__ == "__main__":
    main()