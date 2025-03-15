from partsbox_api import *

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
            
            part_data = get_part_data(part_id, api_key)

            storage_id = part_data[3]
            storage_location = find_storage_name_by_id(storage_id, api_key)

            print(f"Name:\t\t{part_number}")
            print(f"Description:\t{part_data[0]}")
            print(f"Manufacturer:\t{part_data[1]}")
            print(f"Footprint:\t{part_data[2]}")
            print(f"Storage:\t{storage_location}")

            None
        case 2:     # labels from file
            None
        case 3:     # labels for all parts in storage location
            None
        case 4:     # labels for the entire database
            None

if __name__ == '__main__':
    main()