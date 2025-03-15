import requests
import json

# test values for debugging
part_id = "fj7h5erw0rj499evktbvhetc45"
part_num = "CGA0402C0G220J500GT"


def find_part_id_by_number(part_number, api_key):
    # First check the local file to see if we have used this part number before
    # File format is 'partNumber partID'
    with open('partsID.txt') as partsFile:
        set_ids = set([])
        for line in partsFile:
            partNum = line.split(" ")[0].strip()
            partID = line.split(" ")[1].strip()
            set_ids.add(partID)

            if partNum == part_number:
                return partID
    
    # If we got to this point then the part ID does not exist in the file, so we now gotta talk to the API

    # Use API to get all the parts in the database
    url = "https://api.partsbox.com/api/1/part/all"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "APIKey " + api_key
    }
    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
        return -1
    response_data = response.json()
    # Extract the part data list from the 'data' field
    parts_list = response_data.get('data', [])
    # Initialize an empty dictionary to store the processed parts
    parts_dict = {}
    # Loop through each part in the 'data' list
    for part in parts_list:
        # Extract 'part/id' as the key
        part_id = part.get('part/id')
        part_name = part.get('part/name')
        if part_id:
            parts_dict[part_id] = part_name
    
    # Since we polled the API lets reconcile with the local file to prevent the API call again until new parts are added
    with open('partsID.txt', 'a') as partsFile:
        for key in parts_dict:
            if key not in set_ids:
                partsFile.write(f"{parts_dict[key]} {key}\n")
                print(f"Added ID {key} for part number {parts_dict[key]} to local file.")
        
    # Now parts_dict has the ID
    for key in parts_dict:
        if parts_dict[key] == part_number:
            return key
    
    # We got all the way here and did not find it so there was an error
    return -1

# We use part numbers to find their ID, then we can use the part ID to get information about the part
# Part of that information is the storage location ID, but thats no human readable so we need to
# reverse lookup for that string
def find_storage_name_by_id(storage_id, api_key):
    None

if __name__ == '__main__':
    with open("secrets.txt", 'r') as file:
            first_line = file.readline().strip()
            api_key = first_line.split(",")[1]
    print(find_part_id_by_number(part_num, api_key))