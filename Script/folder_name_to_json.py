import json
import os

def create_zip_list_json():
    # Find all .zip files in the current directory
    zip_files = [f for f in os.listdir() if f.endswith(".zip")]

    # Create JSON structure
    zip_data = {"files": zip_files}

    # Save to data.json
    with open("data.json", "w") as json_file:
        json.dump(zip_data, json_file, indent=4)

    print("Created data.json with all .zip file names.")

# Run the function
create_zip_list_json()
