import json
import os

def create_zip_list_json(path):
    # Find all .zip files in the current directory
    zip_files = [f for f in os.listdir(path) if f.endswith(".zip")]

    # Create JSON structure
    zip_data = {"count": len(zip_files), "files": zip_files}

    # Save to data.json
    with open(os.path.join(path, "data.json"), "w") as json_file:
        json.dump(zip_data, json_file, indent=4)

    print("Created data.json with all .zip file names in the given path.")

# Run the function
create_zip_list_json(r"D:\Python\Git repos\manifest_files\manifest_files")