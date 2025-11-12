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
├── README.md (main project documentation)
│
└── src/
    ├── hello_world/
    │   ├── README.md
    │   └── hello_world.py
    │
    ├── calculator/
    │   ├── README.md
    │   └── calculator.py
    │
    └── file_organizer/
        ├── README.md
        ├── SCHEDULING_GUIDE.md
        ├── organizer.py
        └── scheduler.py
```

## Projects

### 1. Hello World
A simple introductory program that prints "Hello, World!" to demonstrate basic Python syntax.

**Location:** `src/hello_world/`

**Running the Program:**
```bash
# From hello_world folder
python hello_world.py

# From project root
python src/hello_world/hello_world.py
```

**Expected Output:**
```
Hello, World!
```

**Module Documentation:**
See `src/hello_world/README.md` for detailed documentation.

---

### 2. Simple Calculator
An interactive calculator application that performs basic arithmetic operations.

**Location:** `src/calculator/`

**Features:**
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with zero division protection)
- Error handling for invalid inputs
- Interactive command-line menu

**Running the Program:**
```bash
# From calculator folder
python calculator.py

# From project root
python src/calculator/calculator.py
```

**Example Usage:**
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

**Module Documentation:**
See `src/calculator/README.md` for detailed documentation.

---

### 3. File Organizer
An intelligent file organization system with automatic file categorization and scheduling capabilities.

**Location:** `src/file_organizer/`

**Module Contents:**
- `organizer.py` - Main file organization script
- `scheduler.py` - Automated scheduling wrapper
- `README.md` - Module-specific documentation

**Features:**
- 📁 Automatically organizes files into category folders
- 🎨 Supports Images, Documents, Videos, Audio, Archives, Code, Executables, Data, and more
- ⚠️ Handles file name conflicts automatically
- 📊 Provides detailed organization summary
- 🔒 Permission and error handling
- 💾 Takes directory path as a command-line parameter
- ⏰ Optional scheduling for automated runs

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

**Running Immediate Organization:**
```bash
# From file_organizer folder
python organizer.py <directory_path>

# From project root
python src/file_organizer/organizer.py <directory_path>
```

**Running Scheduled Organization:**
```bash
# From file_organizer folder
python scheduler.py <directory_path> <frequency> <time>

# From project root
python src/file_organizer/scheduler.py <directory_path> <frequency> <time>
```

**Examples:**
```bash
# Organize Downloads folder immediately
python organizer.py C:\Users\YourName\Downloads

# Organize daily at 9:00 AM
python scheduler.py C:\Users\YourName\Downloads daily 09:00

# Organize every hour
python scheduler.py C:\Users\YourName\Downloads hourly 60

# Organize every Monday at 10:00 AM
python scheduler.py C:\Users\YourName\Downloads weekly monday 10:00
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

**Module Documentation:**
See `src/file_organizer/README.md` for detailed module documentation.

**Scheduling Documentation:**
See `src/file_organizer/SCHEDULING_GUIDE.md` for comprehensive scheduling guide covering Windows Task Scheduler, Linux cron, and Python scheduler methods.

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