# CodeAlpha Internship — Task 3
## Task Automation with Python Scripts

### Project Overview
This project automates the process of moving all JPG image files from a source folder to a destination folder using Python.

### Objective
To reduce repetitive manual work by automatically identifying and moving JPG files between folders.

### Features
- Accepts source and destination folder paths from the user.
- Detects JPG files, including filenames with uppercase extensions.
- Creates the destination folder if it does not exist.
- Moves JPG files automatically.
- Skips files when a file with the same name already exists in the destination.
- Displays the number of files moved.

### Technologies Used
- Python 3
- os module
- shutil module
- Visual Studio Code

### How to Run
1. Install Python 3.
2. Save the script as `File_Automation.py`.
3. Open a terminal in the project directory.
4. Run:

   `python File_Automation.py`

5. Enter the source folder path.
6. Enter the destination folder path.

### Sample Output
```text
Moved: download (1).jpg
Moved: download (2).jpg
Moved: download.jpg

Automation completed! Files moved: 3
```

### Concepts Learned
- File and directory handling
- Python loops and conditional statements
- Working with file paths
- Automating repetitive tasks
- Using Python's os and shutil modules

### Author
Aditya Desai

### Internship
CodeAlpha — Python Programming Internship

### Disclaimer
Tested using sample JPG images. Use test files before running the script on important folders.