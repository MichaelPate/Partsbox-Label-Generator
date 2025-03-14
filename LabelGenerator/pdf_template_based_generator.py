from reportlab.pdfgen import canvas
from PIL import Image

def generate_pdf_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file):
    # Convert label size from mm to points (1 mm = 2.83465 points)
    label_width_points = label_width_mm * 2.83465
    label_height_points = label_height_mm * 2.83465

    # Create the PDF canvas with the specified label size
    c = canvas.Canvas(output_file, pagesize=(label_width_points, label_height_points))

    # Set font
    c.setFont("Helvetica-Bold", 8)
    # Draw text on the PDF (adjust positioning based on the label size)
    c.drawString(10, label_height_points - 14, f"{part_number}")
    c.line(5, label_height_points - 18, label_width_points - 60, label_height_points - 18)

    c.setFont("Helvetica", 8)
    c.drawString(10, label_height_points - 28, f"Category: {category}")
    c.drawString(10, label_height_points - 38, f"Mfg.: {manufacturer}")
    c.drawString(10, label_height_points - 48, f"{storage_location}")

    c.line(5, label_height_points - 52, label_width_points - 60, label_height_points - 52)
    # If the description is too long, split it at a predetermined length and display that, (41 chars)
    # then display the remaining on the line below it. After that it just gets truncated.
    if len(description) > 42:
        c.drawString(10, label_height_points - 64, f"{description[:41]}")
        if (description[41] == ' '):

            c.drawString(10, label_height_points - 73, f"{description[42:83]}")
        else:
            c.drawString(10, label_height_points - 73, f"{description[41:83]}")
    else:
        c.drawString(10, label_height_points - 64, f"{description}")

    # Set a fixed size for the QR code (for example, 20mm x 20mm)
    qr_code_size_mm = 18  # Set the size in mm
    qr_code_size_points = qr_code_size_mm * 2.83465  # Convert to points

    # Adjust the position of the QR code to fit within the label (bottom-right corner)
    qr_code_x = label_width_points - qr_code_size_points - 5  # 10pt margin from right
    qr_code_y = label_height_points - qr_code_size_points - 5  # 10pt margin from the top

    # Draw the QR code image with the fixed size
    c.drawImage(qr_code_path, qr_code_x, qr_code_y, qr_code_size_points, qr_code_size_points)

    # Save the PDF
    c.save()

    print(f"Label PDF saved to {output_file}")

# Example usage
part_number = "CR0402-JW-103GLF"
category = "PCB Stencil"
manufacturer = "Bourns Inc."
description = "RES SMD 10K OHM 5% 1/16W 0402"# RES SMD 10K OHM 5% 1/16W 0402 RES SMD 10K OHM 5% 1/16W 0402"
storage_location = "SMD Magazine A → Cartridge A2"
qr_code_path = "C:\\Users\\LittleBitchBoy\\Documents\\Projects\\Partsbox Label Generator\\Partsbox-Label-Generator\\LabelGenerator\\qr_code_test.png"
label_width_mm = 73  # Label width in mm
label_height_mm = 29  # Label height in mm
output_file = "label.pdf"

generate_pdf_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file)
