# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import os
                  #Byte Maze Hashim
destination_dir = r'F:\git\generate_receipt'

os.makedirs(destination_dir, exist_ok=True)

# Data which we are going to display as tables
DATA = [
    ["Date", "Brand", "Model", "Description", "Price(Rs.)"],
    [
        "01/03/2024",
        "BMW",
        "BMW 7 Series",
        "Luxury Sedan",
        "900,000.00/-",
    ],
    [
        "01/03/2024",
        "Mercedes-Benz",
        "Mercedes-Benz S-Class",
        "Flagship Luxury Sedan ",
        "1,000,000.00/-",
    ],
    [
        "01/03/2024",
        "Porsche",
        "Porsche Panamera",
        "High-Performance Luxury Sports Sedan",
        "1,200,000.00/-",
    ],
    [
        "01/03/2024",
        "Jaguar",
        "Jaguar XJ",
        "Elegant Luxury Sedan",
        "850,000.00/-",
    ],
    [
        "01/03/2024",
        "Audi",
        "Audi A8",
        "Executive Sedan",
        "950,000.00/-",
    ],
    ["Sub Total", "", "", "", "4,900,000.00/-"],
    ["Discount", "", "", "", "-500,000.00/-"],
    ["Total", "", "", "", "4,400,000.00/-"],
]

# Creating a Base Document Template of page size A4
pdf = SimpleDocTemplate(os.path.join(destination_dir, "car_receipt.pdf"), pagesize=A4)

# Standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# Fetching the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# Creating the paragraph with
# the heading text and passing the styles of it
title = Paragraph("Byte Maze Hashim", title_style)

# Define column widths
col_widths = [60, 80, 120, 240, 80]

# Create the table
table = Table(DATA, colWidths=col_widths)

# Apply styles
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 1), (-1, 1), colors.beige),
]))

# Build PDF
pdf.build([title, table])
