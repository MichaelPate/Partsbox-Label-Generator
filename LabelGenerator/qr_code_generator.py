import qrcode

def generate_qr_code(data, output_file):
    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,  # Version determines the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size (in boxes)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image as a PNG file
    img.save(output_file)

'''
# Example usage
data = "Hello, this is a test QR code!"  # This is the string to encode
output_file = "qr_code.png"  # The name of the output file

generate_qr_code(data, output_file)
print(f"QR code saved as {output_file}")
'''