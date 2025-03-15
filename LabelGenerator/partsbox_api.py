import requests
import json
import ast

# test values for debugging
#part_id = "fj7h5erw0rj499evktbvhetc45"
#part_num = "CGA0402C0G220J500GT"


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
    url = "https://api.partsbox.com/api/1/storage/get"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "APIKey " + api_key
    }
    data = {
        "storage/id": storage_id
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
        return -1
    response_data = response.json()
    #print(response_data)

    storage_data = response_data.get('data', [])
    storage_name = storage_data.get('storage/name')
    #print(storage_name)
    return storage_name



def get_part_data(part_id, api_key):
    # Use API to get all the parts in the database
    url = "https://api.partsbox.com/api/1/part/get"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "APIKey " + api_key
    }
    data = {
        "part/id": part_id
    }   
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
        return -1
    response_data = response.json()
    # Extract the part data list from the 'data' field
    parts_data = response_data.get('data', [])
    #print(parts_data)
    part_description = parts_data.get('part/description', 'None')
    part_manufacturer = parts_data.get('part/manufacturer', 'None')
    part_footprint = parts_data.get('part/footprint', 'None')
    #print(parts_data.get('part/stock'))


    stock_data_str = str(parts_data.get('part/stock'))
    part_stock_storage_id = ast.literal_eval(stock_data_str)[0]['stock/storage-id']
    #print(part_stock_storage_id)

    #part_storage_id = parts_data.get('part/stock')[0]['stock/storage-id']

    return [part_description, part_manufacturer, part_footprint, part_stock_storage_id]#part_storage_id]
    

    # Define the URL for the API endpoint
    url = 'https://api.partsbox.com/api/1/part/get'

    # Define the API key (replace with your actual API key)
    headers = {
        'Authorization': 'APIKey ' + api_key,
        'Content-Type': 'application/json',
    }

    # Define the data to be sent in the request (if needed)
    data = {
        "part/id": part_id
    }

    # Send the POST request and get the response
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and get the data
        response_data = response.json()  # Convert JSON to a Python dictionary

        # Print the parsed JSON data
        #print("Response Data:", response_data)
        
        # Extract the 'data' field
        if 'data' in response_data:
            parts_data = response_data['data']
            #print("Parts Data:", parts_data)
            return response_data
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    with open("secrets.txt", 'r') as file:
            first_line = file.readline().strip()
            api_key = first_line.split(",")[1]