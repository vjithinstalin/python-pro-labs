# Python Pro Labs

A collection of Python projects for learning and practice. This repository contains beginner-friendly projects that demonstrate fundamental Python concepts and practical applications.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or navigate to the repository:
```bash
cd python-pro-labs
```

2. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Run any project:
```bash
python src/<project_name>.py
```

## Project Structure

```
python-pro-labs/
│
└── src/
    ├── hello_world.py
    ├── calculator.py
    └── file_organizer.py
```

## Projects

### 1. Hello World
A simple introductory program that prints "Hello, World!" to demonstrate basic Python syntax.

**File:** `src/hello_world.py`

**Running the Program:**
```bash
python src/hello_world.py
```

**Expected Output:**
```
Hello, World!
```

---

### 2. Simple Calculator
An interactive calculator application that performs basic arithmetic operations.

**File:** `src/calculator.py`

**Features:**
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with zero division protection)
- Error handling for invalid inputs
- Interactive command-line menu

**Running the Program:**
```bash
python src/calculator.py
```

**Usage:**
1. Run the program
2. Select an operation (1-5)
3. Enter two numbers
4. View the result
5. Continue with more operations or select option 5 to exit

**Example Output:**
```
Simple Calculator
----------------------------------------
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
----------------------------------------

Enter choice (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
```

---

### 3. File Organizer
An intelligent file organization tool that automatically categorizes and moves files into folders based on their type.

**File:** `src/file_organizer.py`

**Features:**
- 📁 Automatically organizes files into category folders
- 🎨 Supports Images, Documents, Videos, Audio, Archives, Code, Executables, Data, and more
- ⚠️ Handles file name conflicts automatically
- 📊 Provides detailed organization summary
- 🔒 Permission and error handling
- 💾 Takes directory path as a command-line parameter

**Supported File Categories:**
- **Images:** jpg, jpeg, png, gif, bmp, svg, webp, ico, tiff
- **Documents:** pdf, doc, docx, txt, xlsx, xls, ppt, pptx, odt
- **Videos:** mp4, avi, mkv, mov, wmv, flv, webm, m4v
- **Audio:** mp3, wav, flac, aac, ogg, wma, m4a, aiff
- **Archives:** zip, rar, 7z, tar, gz, bz2, iso
- **Code:** py, js, html, css, java, cpp, c, php, rb, go, rs
- **Executables:** exe, msi, bat, cmd, sh, app, dmg
- **Data:** json, xml, csv, sql, db, yml, yaml
- **Other:** Files with unrecognized extensions

**Running the Program:**
```bash
python src/file_organizer.py <directory_path>
```

**Examples:**
```bash
# Organize Downloads folder on Windows
python src/file_organizer.py C:\Users\YourName\Downloads

# Organize Documents folder on macOS/Linux
python src/file_organizer.py /home/user/Documents

# Organize current directory
python src/file_organizer.py .
```

**Sample Output:**
```
============================================================
File Organizer - Organizing: C:\Users\JohnDoe\Downloads
============================================================

✓ Created folder: Images
✓ Created folder: Documents
✓ Created folder: Archives
→ Moved: photo.jpg → Images/
→ Moved: report.pdf → Documents/
→ Moved: backup.zip → Archives/

============================================================
Organization Summary
============================================================
Files organized: 3
Files skipped: 0
Errors: 0

Files by category:
  Archives: 1 file(s)
  Documents: 1 file(s)
  Images: 1 file(s)
============================================================
```

**Important Notes:**
- ⚠️ The organizer only moves files in the specified directory, not in subdirectories
- 🔄 If a file with the same name exists in the destination folder, it will be renamed with a counter (e.g., filename_1.ext)
- Hidden files and folders (starting with '.') are skipped
- Requires appropriate read/write permissions for the target directory

## Requirements

- Python 3.7 or higher

## Setup

This project uses a virtual environment for dependency management. To activate it:

```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

## 📚 Learning Path

1. **Start with Hello World** - Understand basic Python syntax
2. **Try the Calculator** - Learn functions, conditionals, and error handling
3. **Use File Organizer** - Practice file I/O, modules, and command-line arguments

## 💡 Project Summary

| Project | Type | Difficulty | Key Concepts |
|---------|------|------------|--------------|
| Hello World | Basic | Beginner | Print, main() |
| Calculator | Interactive | Beginner | Functions, loops, conditionals |
| File Organizer | Utility | Intermediate | File I/O, OS operations, CLI args |

## 🎯 Next Steps

- Extend the calculator with more operations (power, square root, etc.)
- Add a GUI to the calculator using tkinter
- Create a scheduling feature for automatic file organization
- Add logging to track file operations
- Create unit tests for each project

## 📝 Notes

- All projects are designed for educational purposes
- Feel free to modify and extend these projects
- Use these as templates for your own Python applications

## 📄 License

This project is open source and available for learning purposes.

## Contributing

Feel free to expand these projects with additional features or create new ones!