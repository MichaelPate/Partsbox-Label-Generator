import requests
import json


with open("secrets.txt", 'r') as file:
        first_line = file.readline().strip()
        api_key = first_line.split(",")[1]

part_id = "fj7h5erw0rj499evktbvhetc45"

'''
# Define the API endpoint and headers
url = "https://api.partsbox.com/api/1/part/all"
headers = {
    "Content-Type": "application/json",
    "Authorization": "APIKey " + api_key
}

# Define the payload (the data to be sent in the POST request)
data = {
    "part/id": part_id
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the response data (assuming JSON response)
    print("Response Data:", response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:", response.text)
'''

def process_response(response_data):
    # Extract the part data list from the 'data' field
    parts_list = response_data.get('data', [])
    
    # Initialize an empty dictionary to store the processed parts
    parts_dict = {}
    
    # Loop through each part in the 'data' list
    for part in parts_list:
        # Extract 'part/id' as the key
        part_id = part.get('part/id')
        part_name = part.get('part/name')
        #print(f"{part_id}: {part.get('part/name')}")

        if part_id:
            parts_dict[part_id] = part_name

        '''
        # If part_id is found, proceed to process the data
        if part_id:
            # Create a dictionary for the rest of the part data (excluding 'part/id')
            part_details = {key: value for key, value in part.items() if key != 'part/id'}
            
            # Add the part_id and its details to the parts_dict
            parts_dict[part_id] = part_details'
        '''

    return parts_dict

def find_part_id_by_number(part_number, api_key):
    # First check the local file to see if we have used this part number before
    # File format is 'partNumber partID'
    with open('partsID.txt', 'r') as partsFile:
        for line in partsFile:
            partNum = line.split(" ")[0]
            partID = line.split(" ")[1]

            if partNum == part_number:
                return partID

    # If we got to this point then the part ID does not exist in the file, so we gotta talk to the API

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

    # Now we add all the part IDs to our file that dont already exist
    parts_dict = process_response(response.json())

    # Print the resulting dictionary
    print(parts_dict)

if __name__ == '__main__':
    find_part_id_by_number(part_id, api_key)