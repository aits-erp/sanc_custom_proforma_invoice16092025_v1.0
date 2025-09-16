import os
import json

# Find doctype folder inside the app module folder
app_dir = os.path.dirname(__file__)
doctype_dir = None

for item in os.listdir(app_dir):
    potential = os.path.join(app_dir, item, "doctype")
    if os.path.isdir(potential):
        doctype_dir = potential
        break

if not doctype_dir:
    print("Error: Could not find a 'doctype' folder inside the app module.")
    exit(1)

# Loop through all DocType folders and JSONs
for folder_name in os.listdir(doctype_dir):
    folder_path = os.path.join(doctype_dir, folder_name)
    
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON: {file_path}")
                        continue

                # Only add "name" if missing
                if "name" not in data or not data["name"]:
                    name_value = " ".join(word.capitalize() for word in folder_name.split("_"))
                    data["name"] = name_value
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    print(f"Added name: {file_path}")
                else:
                    print(f"Already has name: {file_path}")
