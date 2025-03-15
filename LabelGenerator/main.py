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
    
    match option:
        case 1:     # one label from one part number
            part_number = input("Please enter the part number: ")
            
            None
        case 2:     # labels from file
            None
        case 3:     # labels for all parts in storage location
            None
        case 4:     # labels for the entire database
            None

if __name__ == '__main__':
    main()