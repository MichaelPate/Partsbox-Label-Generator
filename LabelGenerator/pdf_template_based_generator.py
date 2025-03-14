from reportlab.pdfgen import canvas
from PIL import Image

def generate_pdf_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file):
    # Convert label size from mm to points (1 mm = 2.83465 points)
    label_width_points = label_width_mm * 2.83465
    label_height_points = label_height_mm * 2.83465

    # Create the PDF canvas with the specified label size
    c = canvas.Canvas(output_file, pagesize=(label_width_points, label_height_points))

    # Set font
    c.setFont("Helvetica", 8)

    # Draw text on the PDF (adjust positioning based on the label size)
    c.drawString(10, label_height_points - 20, f"Part Number: {part_number}")
    c.drawString(10, label_height_points - 40, f"Category: {category}")
    c.drawString(10, label_height_points - 60, f"Manufacturer: {manufacturer}")
    c.drawString(10, label_height_points - 80, f"Description: {description}")
    c.drawString(10, label_height_points - 100, f"Storage Location: {storage_location}")

    # Set a fixed size for the QR code (for example, 20mm x 20mm)
    qr_code_size_mm = 20  # Set the size in mm
    qr_code_size_points = qr_code_size_mm * 2.83465  # Convert to points

    # Adjust the position of the QR code to fit within the label (bottom-right corner)
    qr_code_x = label_width_points - qr_code_size_points - 10  # 10pt margin from right
    qr_code_y = 10  # 10pt margin from the bottom

    # Draw the QR code image with the fixed size
    c.drawImage(qr_code_path, qr_code_x, qr_code_y, qr_code_size_points, qr_code_size_points)

    # Save the PDF
    c.save()

    print(f"Label PDF saved to {output_file}")

# Example usage
part_number = "12345"
category = "Electronics"
manufacturer = "Example Corp"
description = "This is an example item description"
storage_location = "A1-03"
qr_code_path = "C:\\Users\\LittleBitchBoy\\Documents\\Projects\\Partsbox Label Generator\\Partsbox-Label-Generator\\LabelGenerator\\qr_code_test.png"
label_width_mm = 73  # Label width in mm
label_height_mm = 29  # Label height in mm
output_file = "label.pdf"

generate_pdf_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file)
