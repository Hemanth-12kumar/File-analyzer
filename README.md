# Desktop File Organizer Bot
Project Overview
The Desktop File Organizer Bot is a Python automation tool that helps organize files in a directory.  
It categorizes files like PDFs, images, and documents into separate folders automatically, reducing manual file management and improving productivity.

---
 Features
- Rule-based file organization by file type:
  - PDFs
  - Images (JPG, PNG, GIF, etc.)
  - Documents (DOCX, TXT, PPTX, XLSX, etc.)
  - Others (for uncategorized files)
- Automatically creates folders if they do not exist
- Simple and easy-to-run Python script
- Can be customized for any folder or file type

---
 Tech Stack
- Python (Programming language)
- OS Module (Access and manipulate the file system)
- Shutil Module (Move files between folders)

---
How It Works
1. Scans the target folder (default: Desktop)
2. Checks the file extension of each file
3. Moves the file into the corresponding folder
4. Creates an "Others" folder for uncategorized files
5. Prints a success message when done

---


