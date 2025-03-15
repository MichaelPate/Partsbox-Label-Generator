from reportlab.pdfgen import canvas
from PIL import Image

def generate_pdf_label(part_number, footprint, manufacturer, description, storage_location, qr_code_path, output_file, template):
    if template == 'Standard':
        label_height_mm = 29
        label_width_mm = 73
    elif template == 'Magazine-Legacy':
        label_height_mm = 29
        label_width_mm = 65
    elif template == 'Magazine':
        label_height_mm = 38
        label_width_mm = 65

    # Convert label size from mm to points (1 mm = 2.83465 points)
    label_width_points = label_width_mm * 2.83465
    label_height_points = label_height_mm * 2.83465

    # Create the PDF canvas with the specified label size
    c = canvas.Canvas(output_file, pagesize=(label_width_points, label_height_points))

    # Standard label is 29mm continuous tape, with a 73mm label width
    if (template == 'Standard'):
        maxLineLength = 42

        c.setFont("Helvetica-Bold", 8)
        c.drawString(10, label_height_points - 14, f"{part_number[:30]}")
        c.line(5, label_height_points - 18, label_width_points - 60, label_height_points - 18)
        c.setFont("Helvetica", 8)
        c.drawString(10, label_height_points - 28, f"Footprint: {footprint[:22]}")
        c.drawString(10, label_height_points - 38, f"Mfg.: {manufacturer[:27]}")
        c.drawString(10, label_height_points - 48, f"{storage_location[:32]}")
        c.line(5, label_height_points - 52, label_width_points - 60, label_height_points - 52)
        # If the description is too long, split it at a predetermined length and display that,
        # then display the remaining on the line below it. After that it just gets truncated.
        if len(description) > maxLineLength:
            c.drawString(10, label_height_points - 64, f"{description[:maxLineLength-1]}")
            if (description[maxLineLength-1] == ' '):

                c.drawString(10, label_height_points - 73, f"{description[maxLineLength:maxLineLength*2-2]}")
            else:
                c.drawString(10, label_height_points - 73, f"{description[maxLineLength-1:maxLineLength*2-2]}")
        else:
            c.drawString(10, label_height_points - 64, f"{description}")

        # Set a fixed size for the QR code
        qr_code_size_mm = 18
        qr_code_size_points = qr_code_size_mm * 2.83465
        qr_code_x = label_width_points - qr_code_size_points - 5  # 5pt margin from right
        qr_code_y = label_height_points - qr_code_size_points - 5  # 5pt margin from the top
        c.drawImage(qr_code_path, qr_code_x, qr_code_y, qr_code_size_points, qr_code_size_points)

    # Magazine legacy label is 29mm continuous tape, with a 65mm label width
    elif template == 'Magazine-Legacy':
        maxLineLength = 24
        '''
        Differences from standard label
        Assumptions:
            Its an SMD cartridge mounted in a magazine, so the part numbers can be longer
            and the manufacturer is not important.
        
        Design:
            Two lines available for part number and description and storage location.
            The manufacturer field is not shown, and footprint is still one line
        '''

        c.setFont("Helvetica-Bold", 8)

        #c.drawString(10, label_height_points - 14, f"{part_number}")
        if len(part_number) > maxLineLength:
            c.drawString(10, label_height_points - 14, f"{part_number[:maxLineLength-1]}")
            if (part_number[maxLineLength-1] == ' '):

                c.drawString(10, label_height_points - (14+9), f"{part_number[maxLineLength:maxLineLength*2]}")
            else:
                c.drawString(10, label_height_points - (14+9), f"{part_number[maxLineLength-1:maxLineLength*2]}")
        else:
            c.drawString(10, label_height_points - 14, f"{part_number}")

        #c.line(5, label_height_points - 18, label_width_points - 60, label_height_points - 18)
        c.setFont("Helvetica", 8)
        c.drawString(10, label_height_points - 32, f"Footprint: {footprint[:18]}")
        #c.drawString(10, label_height_points - 38, f"Mfg.: {manufacturer}")

        #c.drawString(10, label_height_points - 41, f"{storage_location}")
        if len(storage_location) > maxLineLength:
            c.drawString(10, label_height_points - 41, f"{storage_location[:maxLineLength-1]}")
            if (storage_location[maxLineLength-1] == ' '):

                c.drawString(10, label_height_points - (41+9), f"{storage_location[maxLineLength:maxLineLength*2]}")
            else:
                c.drawString(10, label_height_points - (41+9), f"{storage_location[maxLineLength-1:maxLineLength*2]}")
        else:
            c.drawString(10, label_height_points - 41, f"{storage_location}")

        c.line(5, label_height_points - 54, label_width_points - 60, label_height_points - 54)
        # If the description is too long, split it at a predetermined length and display that, (41 chars)
        # then display the remaining on the line below it. After that it just gets truncated.
        
        maxLineLength = 33
        if len(description) > maxLineLength:
            c.drawString(10, label_height_points - 64, f"{description[:maxLineLength-1]}")
            if (description[maxLineLength-1] == ' '):

                c.drawString(10, label_height_points - 73, f"{description[maxLineLength:maxLineLength*2]}")
            else:
                c.drawString(10, label_height_points - 73, f"{description[maxLineLength-1:maxLineLength*2]}")
        else:
            c.drawString(10, label_height_points - 64, f"{description}")

        # Set a fixed size for the QR code
        qr_code_size_mm = 18
        qr_code_size_points = qr_code_size_mm * 2.83465
        qr_code_x = label_width_points - qr_code_size_points - 5  # 5pt margin from right
        qr_code_y = label_height_points - qr_code_size_points - 5  # 5pt margin from the top
        c.drawImage(qr_code_path, qr_code_x, qr_code_y, qr_code_size_points, qr_code_size_points)

    # Magazine standard label is 38mm continuous tape, with a 65mm label width
    elif template == 'Magazine':
        None
        #TODO Implement magazine labels, essentially the same as magazine-legacy but with more vertical room

    # Save the PDF
    c.save()
    print(f"Label PDF saved to {output_file}")




# Example usage
part_number = "JLC-Y18-2195815A-PCBLC-Y18-2195815A-PCBLC-Y18-2195815A-PCB"
footprint = "PCB Stencil123456789123456789"
manufacturer = "Bourns Inc.1234567890123456789012345678909"
description = "RES SMD 10K OHM 5% 1/16W 0402 RES SMD 10K OHM 5% 1/16W 0402 RES SMD 10K OHM 5% 1/16W 0402"
storage_location = "SMD Magazine A → Cartridge A21234567891234567890"
qr_code_path = "C:\\Users\\LittleBitchBoy\\Documents\\Projects\\Partsbox Label Generator\\Partsbox-Label-Generator\\LabelGenerator\\qr_code_test.png"
label_width_mm = 73  # Label width in mm
label_height_mm = 29  # Label height in mm
output_file = "label.pdf"

template = "Magazine-Legacy" # template for formatting the data on the label

generate_pdf_label(part_number, footprint, manufacturer, description, storage_location, qr_code_path, output_file, template)
