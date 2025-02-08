import json
import os

def rename_zip_files():
    # Load data.json
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    # Iterate through each file entry in the JSON
    for entry in data["files"]:
        original_name = entry["fileName"]
        app_id = entry["appID"]
        new_name = f"{app_id}.zip"

        # Check if the file exists in the directory
        if os.path.exists(original_name):
            os.rename(original_name, new_name)
            print(f'Renamed: "{original_name}" -> "{new_name}"')
        else:
            print(f'File not found: "{original_name}"')

# Run the function
rename_zip_files()
