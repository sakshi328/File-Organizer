import os

def organize_uploaded_files(files, destination_folder):
    for file in files:
        # Get the filename including relative folder structure
        filename = file.filename  # e.g., "New folder/cartoon girl.jpg"
        ext = filename.split(".")[-1].upper()  # File extension

        # Create full path for saving
        ext_folder = os.path.join(destination_folder, ext)
        full_path = os.path.join(ext_folder, filename)  # includes subfolders

        # Ensure all folders in the path exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Save the file
        file.save(full_path)
