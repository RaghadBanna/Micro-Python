import os
import shutil

def sort_files(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get list of files in source directory
    files = os.listdir(source_dir)

    # Iterate through files and move them to appropriate folders
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            # Get file extension
            _, extension = os.path.splitext(file)
            # Destination directory for the file based on extension
            dest_folder = os.path.join(destination_dir, extension[1:].lower())
            # Create destination folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            # Move file to destination folder
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_folder, file))

if __name__ == "__main__":
    # Source directory containing files to be sorted
    source_directory = input("Enter the path of the directory to sort: ")
    # Destination directory to move sorted files
    destination_directory = input("Enter the path of the destination directory: ")
    # Sort files
    sort_files(source_directory, destination_directory)
    print("Files sorted successfully.")
