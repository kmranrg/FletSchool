import os

def clear_qr_codes():
    folder_path = "assets/qr"
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Get a list of all files in the folder
        files_in_folder = os.listdir(folder_path)
        
        # Iterate through the files and delete them
        for file in files_in_folder:
            file_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
    else:
        print(f"The folder '{folder_path}' does not exist.")
