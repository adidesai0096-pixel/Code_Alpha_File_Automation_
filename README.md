# CodeAlpha Internship — Task 3
## Task Automation with Python Scripts

### 📌 Project Overview
This project automates the process of moving JPG image files from a source folder to a destination folder using Python. It reduces repetitive manual work and demonstrates basic file management and automation.

### 🎯 Objective
To develop a Python script that automatically identifies JPG files in a specified source directory and moves them to a destination directory.

### ✨ Features
- Accepts source and destination folder paths from the user.
- Identifies `.jpg` files, including uppercase `.JPG` extensions.
- Automatically creates the destination folder if it does not exist.
- Moves JPG files to the destination folder.
- Skips files when a file with the same name already exists in the destination.
- Displays each moved filename and the total number of files moved.
- Handles an invalid source folder path.

### 🛠️ Technologies Used
- **Language:** Python 3
- **Modules:** `os`, `shutil`
- **Editor:** Visual Studio Code
- **Platform:** Windows

### 📂 Project Structure
```text
CodeAlpha_Task3_FileAutomation/
├── File_Automation.py
└── README.md
```

### ⚙️ Requirements
- Python 3 installed on your computer.
- No external Python packages are required.

### ▶️ How to Run

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

   ```bash
   python File_Automation.py
   ```

5. Enter the full path of the source folder.
6. Enter the full path of the destination folder.
7. Check the destination folder to verify the moved images.

### 💻 Sample Output
```text
Moved: download (1).jpg
Moved: download (2).jpg
Moved: download.jpg

Automation completed! Files moved: 3
```

*Note: The filenames
