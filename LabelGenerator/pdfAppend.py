import PyPDF2
import os

# Function to merge multiple PDF files into one output PDF
def merge_pdfs(input_files, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through all the input files
    for input_pdf in input_files:
        if os.path.exists(input_pdf):
            # Open the current input PDF
            with open(input_pdf, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                # Check if the input PDF has pages, and add each page to the writer
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
        else:
            print(f"Warning: The file '{input_pdf}' does not exist.")
    
    # Write the combined content to the output PDF
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"PDF created: {output_pdf}")

'''
# List of input PDF files (change this list to match your input files)
input_pdfs = ["GeneratedLabels\\label_CGA0402C0G220J500GT.pdf", "GeneratedLabels\\label_CR0402-JW-103GLF.pdf"]

# Output PDF file
output_pdf = "GeneratedLabels\\combined_output.pdf"

# Merge the PDFs
merge_pdfs(input_pdfs, output_pdf)'
'''