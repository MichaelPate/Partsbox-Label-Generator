from partsbox_api import *
from qr_code_generator import *
from pdf_template_based_generator import *
from pdfAppend import *
import webbrowser, re, os


def main():
    mainMenuSelectionMade = False
    while not mainMenuSelectionMade:
        print("+----------------------------------------------------------+")
        print("| Welcome to the Partsbox Label Generator!                 |")
        print("+----------------------------------------------------------+")
        print("| Please select an operation:                              |")
        print("+----------------------------------------------------------+")
        print("| 1. Generate single label from part number                |")
        print("| 2. Generate multiple labels from file                    |")
        print("| 3. Generate labels for all parts in a storage location   |")
        print("| 4. Generate labels for all parts in your database        |")
        print("+----------------------------------------------------------+")
        option = input("Please enter your selection: ")
        if option.isnumeric():
            option = int(option)
            if option >= 1 and option <= 4:
                mainMenuSelectionMade = True
            else:
                print("INVALID SELECTION!")
        else:
            print("INVALID SELECTION!")
    
    with open("secrets.txt", 'r') as file:
            first_line = file.readline().strip()
            api_key = first_line.split(",")[1]

    match option:
        case 1:     # one label from one part number
            part_number = input("Please enter the part number: ")
            part_id = find_part_id_by_number(part_number, api_key)

            if part_id == -1:
                print("That part number does not exist!")
            else:
                part_data = get_part_data(part_id, api_key)
                storage_id = part_data[3]
                storage_location = find_storage_name_by_id(storage_id, api_key)
                print(f"Found it! Check details below for part number {part_number}")
                print(f"Description:\t{part_data[0]}")
                print(f"Manufacturer:\t{part_data[1]}")
                print(f"Footprint:\t{part_data[2]}")
                print(f"Storage:\t{storage_location}")

                # generate a QR code using the part number
                qr_code_filename = "GeneratedCodes\\code_" + str(part_number) + ".png"
                generate_qr_code(part_number, qr_code_filename)

                # Call up the label generator
                #generate_pdf_label(part_number, category, manufacturer, description, storage_location, qr_code_path, output_file, template):
                print("+------------------------------------+")
                print("| Please choose a template style     |")
                print("+------------------------------------+")
                print("| 1. Standard 29x73                  |")
                print("| 2. Magazine Label 29x65            |")
                print("+------------------------------------+")
                option = input("Enter style choice: ")
                if option.isnumeric():
                    option = int(option)
                    if option >= 1 and option <= 2:
                        if option == 1: template_choice = "Standard"
                        else: template_choice = "Magazine-Legacy"
                    else:
                        print("INVALID SELECTION! Using Standard.")
                        template_choice = "Standard"
                else:
                    print("INVALID SELECTION! Using Standard.")
                    template_choice = "Standard"
                label_filename = 'GeneratedLabels\\label_' + str(part_number) + ".pdf"
                generate_pdf_label(part_number, part_data[2], part_data[1], part_data[0], str(storage_location), qr_code_filename, label_filename, template_choice)
                webbrowser.open(label_filename)
                

        case 2:     # labels from file
            generated_labels_files_list = []
            file_valid = False
            while not file_valid:
                print("Ensure that the input file has been placed into the input files folder!")
                print("Ensure the file is formatted with exactly one part number per line!")
                filename_input = input("Enter the filename (ex. inputFile.txt): ")
                if re.match(r'^[a-zA-Z0-9_\-\.]+$', filename_input):
                    # valid filename check to see if it exists
                    check_filename = "InputFiles\\" + filename_input
                    if os.path.exists(check_filename):
                        # this file works! We can read it and attempt to make some labels
                        file_valid = True
                        break
                    else:
                        print("That file does not exist!")
                else:
                    print("That is not a valid file name.")
            
            print("+------------------------------------+")
            print("| Please choose a template style     |")
            print("+------------------------------------+")
            print("| 1. Standard 29x73                  |")
            print("| 2. Magazine Label 29x65            |")
            print("+------------------------------------+")
            option = input("Enter style choice: ")
            if option.isnumeric():
                option = int(option)
                if option >= 1 and option <= 2:
                    if option == 1: template_choice = "Standard"
                    else: template_choice = "Magazine-Legacy"
                else:
                    print("Invalid option number! Using Standard.")
                    template_choice = "Standard"
            else:
                print("Invalid input! Using Standard.")
                template_choice = "Standard"

            line_count = 0
            with open(check_filename, 'r') as input_file:
                for line in input_file:
                    line_count += 1

                    part_number = line.strip()
                    part_id = find_part_id_by_number(part_number, api_key)

                    if part_id == -1:
                        print(f"Line {line_count} does not contain a valid part number! Part number is {part_number}")
                    else:
                        # get the parameters
                        part_data = get_part_data(part_id, api_key)
                        storage_id = part_data[3]
                        part_storage_location = find_storage_name_by_id(storage_id, api_key)
                        part_description = part_data[0]
                        part_manufacturer = part_data[1]
                        part_footprint = part_data[2]
                        print(f"Found part number {part_number}. Generating label.")

                        # generate a QR code using the part number
                        qr_code_filename = "GeneratedCodes\\code_" + str(part_number) + ".png"
                        generate_qr_code(part_number, qr_code_filename)

                        # generate a pdf label
                        label_filename = 'GeneratedLabels\\label_' + str(part_number) + ".pdf"
                        generate_pdf_label(part_number, part_footprint, part_manufacturer, part_description, str(part_storage_location), qr_code_filename, label_filename, template_choice)

                        # add the filename from that label to generated_labels_files_list
                        generated_labels_files_list.append(label_filename)

            # if any, combine all the generated_labels_files_list files into one file
            #append_pdf(output_pdf, pdf_to_add, template)
            output_label_filename = "GeneratedLabels\\bulk_from_" + filename_input.split('.')[0] + ".pdf"
            merge_pdfs(generated_labels_files_list, output_label_filename)

            # open that file for printing
            webbrowser.open(output_label_filename)

        case 3:     # labels for all parts in storage location
            None
        case 4:     # labels for the entire database
            None

if __name__ == '__main__':
    main()