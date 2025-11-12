# File Organizer Module

A complete file organization system with automatic file categorization and scheduling capabilities.

**👤 Creator:** [vjithinstalin](https://github.com/vjithinstalin)

---

## 📁 Files in This Module

### `organizer.py`
The main file organizer script that automatically categorizes and moves files into folders by type.

**Usage:**
```bash
python organizer.py <directory_path>
```

**Example:**
```bash
python organizer.py C:\Users\YourName\Downloads
```

**Features:**
- Automatically detects file types by extension
- Creates category folders automatically
- Handles file name conflicts
- Provides detailed organization statistics

### `scheduler.py`
A scheduling wrapper that runs the file organizer automatically at specified intervals.

**Usage:**
```bash
python scheduler.py <directory_path> [frequency] [time]
```

**Frequency Options:**
- `daily <HH:MM>` - Run every day at specified time
- `hourly <minutes>` - Run every N minutes
- `weekly <day> <HH:MM>` - Run on specific day at time

**Examples:**
```bash
# Run daily at 9:00 AM
python scheduler.py C:\Users\YourName\Downloads daily 09:00

# Run every 60 minutes
python scheduler.py C:\Users\YourName\Downloads hourly 60

# Run every Monday at 10:00 AM
python scheduler.py C:\Users\YourName\Downloads weekly monday 10:00
```

## 🗂️ Supported File Categories

| Category | Extensions |
|----------|-----------|
| **Images** | jpg, jpeg, png, gif, bmp, svg, webp, ico, tiff |
| **Documents** | pdf, doc, docx, txt, xlsx, xls, ppt, pptx, odt |
| **Videos** | mp4, avi, mkv, mov, wmv, flv, webm, m4v |
| **Audio** | mp3, wav, flac, aac, ogg, wma, m4a, aiff |
| **Archives** | zip, rar, 7z, tar, gz, bz2, iso |
| **Code** | py, js, html, css, java, cpp, c, php, rb, go, rs |
| **Executables** | exe, msi, bat, cmd, sh, app, dmg |
| **Data** | json, xml, csv, sql, db, yml, yaml |
| **Other** | Any unrecognized file type |

## 🚀 Quick Start

### Run Once (Immediate Organization)
```bash
cd src/file_organizer
python organizer.py C:\Users\YourName\Downloads
```

### Run on Schedule (Automated)
```bash
cd src/file_organizer
python scheduler.py C:\Users\YourName\Downloads daily 09:00
```

## ⚙️ Requirements

- Python 3.7 or higher
- `schedule` library (for scheduler.py)

Install requirements:
```bash
pip install schedule
```

## 📊 Output Example

```
============================================================
File Organizer - Organizing: C:\Users\YourName\Downloads
============================================================

✓ Created folder: Images
✓ Created folder: Documents
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

## 🔧 Advanced Usage

### Windows Task Scheduler Integration

Use with Windows Task Scheduler for automatic execution:

1. Open Task Scheduler
2. Create a new task with:
   - Program: `C:\path\to\.venv\Scripts\python.exe`
   - Arguments: `src\file_organizer\organizer.py C:\Users\YourName\Downloads`
   - Start in: `C:\Users\YourName\Projects\python-pro-labs`

### Linux/macOS Cron

Add to crontab for automatic scheduling:

```bash
# Daily at 9:00 AM
0 9 * * * cd /home/user/python-pro-labs && /home/user/.venv/bin/python src/file_organizer/organizer.py /home/user/Downloads

# Every hour
0 * * * * cd /home/user/python-pro-labs && /home/user/.venv/bin/python src/file_organizer/organizer.py /home/user/Downloads
```

## 📝 Notes

- Only processes files in the specified directory (not subdirectories)
- Requires read/write permissions for the target directory
- Files without extensions are skipped
- File name conflicts are automatically resolved by adding a counter suffix

## 🐛 Troubleshooting

**Scheduler doesn't run tasks:**
- Check that the `schedule` library is installed
- Verify the directory path exists
- Ensure proper file permissions

**Files not organized:**
- Check the output messages for errors
- Verify the directory path is correct
- Ensure files have recognized extensions

## 📚 Related Files

- `SCHEDULING_GUIDE.md` - Comprehensive scheduling guide for all methods
- `README.md` - This file
- `../../README.md` - Main project documentation
