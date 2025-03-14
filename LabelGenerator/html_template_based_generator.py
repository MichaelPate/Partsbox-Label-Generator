# Use python virtual environment:
# partsbox_labelgen_env
# partsbox_labelgen_env\Scripts\activate


import os
from pathlib import Path

def generate_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file):
    # Convert label size from mm to cm for CSS (easier to work with in CSS)
    label_width_cm = label_width_mm / 10
    label_height_cm = label_height_mm / 10

    # Ensure the QR code path exists
    if not os.path.exists(qr_code_path):
        raise FileNotFoundError(f"QR code image not found at: {qr_code_path}")

    # HTML Template
    label_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Label</title>
        <style>
            .label {{
                width: {label_width_cm}cm;
                height: {label_height_cm}cm;
                padding: 1cm;
                border: 1px solid #000;
                font-family: Arial, sans-serif;
                font-size: 12pt;
            }}
            .label h1 {{
                font-size: 16pt;
                margin-bottom: 5mm;
                text-align: center;
            }}
            .label .qr-code {{
                text-align: center;
                margin-top: 10mm;
            }}
            .label .info {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 5mm;
            }}
            .label .info div {{
                width: 48%;
            }}
            .label .info div label {{
                font-weight: bold;
            }}
            .label .description {{
                margin-top: 10mm;
                font-size: 10pt;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="label">
            <h1>{manufacturer} - {part_number}</h1>
            <div class="info">
                <div><label>Category:</label> {category}</div>
                <div><label>Storage Location:</label> {storage_location}</div>
            </div>
            <div class="info">
                <div><label>Manufacturer:</label> {manufacturer}</div>
                <div><label>Description:</label> {description}</div>
            </div>
            <div class="qr-code">
                <img src="{qr_code_path}" alt="QR Code" width="50mm" />
            </div>
            <div class="description">
                <p>Scan this code for more details</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save the HTML to the output file
    with open(output_file, "w") as file:
        file.write(label_html)

    print(f"Label saved to {output_file}")

# Example usage
part_number = "12345"
category = "Electronics"
manufacturer = "Example Corp"
description = "This is an example item description"
storage_location = "A1-03"
qr_code_path = "C:\\Users\\LittleBitchBoy\\Documents\\Projects\\Partsbox Label Generator\\Partsbox-Label-Generator\\LabelGenerator\\qr_code_test.png"
label_width_mm = 100  # Label width in mm
label_height_mm = 50  # Label height in mm
output_file = "label.html"

generate_label(part_number, category, manufacturer, description, storage_location, qr_code_path, label_width_mm, label_height_mm, output_file)
