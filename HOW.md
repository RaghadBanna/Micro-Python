### How the File Sorter Works:

1. **Import Dependencies:**
    
    - The script starts by importing necessary modules and libraries, including `os` for file and directory operations, and `shutil` for file movement.
2. **Define sort_files Function:**
    
    - The `sort_files` function is defined to handle the sorting process. It takes two parameters: `source_dir` (the directory containing files to be sorted) and `destination_dir` (the directory where sorted files will be moved).
3. **Create Destination Directory:**
    
    - The script checks if the destination directory exists. If not, it creates the directory using `os.makedirs()`.
4. **Retrieve List of Files:**
    
    - It retrieves a list of files in the source directory using `os.listdir()`.
5. **Iterate Through Files:**
    
    - The script iterates through each file in the source directory.
6. **Extract File Extension:**
    
    - For each file, it extracts the file extension using `os.path.splitext()`.
7. **Determine Destination Folder:**
    
    - Based on the file extension, the script determines the destination folder where the file will be moved.
8. **Create Destination Folder:**
    
    - If the destination folder corresponding to the file extension doesn't exist, the script creates it using `os.makedirs()`.
9. **Move File:**
    
    - The file is then moved from the source directory to the destination folder using `shutil.move()`.
10. **Main Block:**
    
    - In the main block, the script prompts the user to input the source and destination directories.
    - It calls the `sort_files` function with the provided directories to initiate the sorting process.
11. **Completion Message:**
    
    - After sorting is completed, the script prints a success message indicating that the files have been sorted successfully.

### Workflow:

- The script organizes files based on their file extensions into separate folders within a specified destination directory.
- It iterates through each file in the source directory, determines the file extension, and moves the file to the appropriate folder in the destination directory.
- The user provides the source directory containing files to be sorted and the destination directory where sorted files will be moved.
- After execution, the files are successfully sorted into respective folders based on their extensions.

### Conclusion:

The File Sorter script provides a convenient solution for organizing files based on their types, enhancing file management and organization. It efficiently handles file sorting tasks, making it easier for users to categorize and manage their files effectively.