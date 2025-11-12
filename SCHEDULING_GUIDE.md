# File Organizer Scheduling Guide

This guide explains how to schedule the file organizer to run automatically at regular intervals.

## Method 1: Using Python Scheduler (Cross-Platform)

This method uses the `schedule` library and works on Windows, macOS, and Linux.

### Installation

The `schedule` package is already installed. If not, run:
```bash
pip install schedule
```

### Usage

Run the scheduler with the following command:

```bash
python src/file_organizer_scheduler.py <directory_path> [frequency] [time]
```

### Examples

#### Daily Scheduling
Run every day at 9:00 AM:
```bash
python src/file_organizer_scheduler.py C:\Users\YourName\Downloads daily 09:00
```

#### Hourly Scheduling
Run every 60 minutes:
```bash
python src/file_organizer_scheduler.py C:\Users\YourName\Downloads hourly 60
```

Run every 30 minutes:
```bash
python src/file_organizer_scheduler.py C:\Users\YourName\Downloads hourly 30
```

#### Weekly Scheduling
Run every Monday at 10:00 AM:
```bash
python src/file_organizer_scheduler.py C:\Users\YourName\Downloads weekly monday 10:00
```

Supported days: monday, tuesday, wednesday, thursday, friday, saturday, sunday

### Features
- ✓ Logs each run with timestamp
- ✓ Provides status updates (success/error)
- ✓ Press Ctrl+C to stop the scheduler
- ✓ Cross-platform compatibility

---

## Method 2: Windows Task Scheduler (Windows Only)

### Steps

1. **Open Task Scheduler**
   - Press `Win + R`
   - Type `taskschd.msc` and press Enter

2. **Create a New Task**
   - Click "Create Basic Task" on the right panel
   - Enter a name: "File Organizer"
   - Enter description: "Automatically organize files"
   - Click Next

3. **Set the Trigger**
   - Choose when the task should run (Daily, Weekly, etc.)
   - Click Next

4. **Set the Action**
   - Select "Start a program"
   - Program: `C:\Users\YourName\Projects\python-pro-labs\.venv\Scripts\python.exe`
   - Arguments: `src\file_organizer.py C:\Users\YourName\Downloads`
   - Start in: `C:\Users\YourName\Projects\python-pro-labs`
   - Click Next

5. **Review and Create**
   - Click Finish to create the task

### Example
**Program/Script:**
```
C:\Users\jithinstalin\Projects\python-pro-labs\.venv\Scripts\python.exe
```

**Arguments:**
```
src\file_organizer.py C:\Users\jithinstalin\Downloads
```

**Start in (optional):**
```
C:\Users\jithinstalin\Projects\python-pro-labs
```

---

## Method 3: Windows Batch Script with Task Scheduler

### Create a Batch File

1. Create a file named `run_organizer.bat` in your project root:

```batch
@echo off
cd /d C:\Users\jithinstalin\Projects\python-pro-labs
.venv\Scripts\python.exe src\file_organizer.py C:\Users\jithinstalin\Downloads
pause
```

2. Schedule this batch file using Windows Task Scheduler (see Method 2)

### Advantages
- Simpler to set up
- Works reliably with Task Scheduler
- Can add logging by redirecting output

---

## Method 4: Linux/macOS Cron

### Edit Crontab

```bash
crontab -e
```

### Add Cron Entry

Run daily at 9:00 AM:
```cron
0 9 * * * cd /home/user/python-pro-labs && /home/user/python-pro-labs/.venv/bin/python src/file_organizer.py /home/user/Downloads
```

Run every hour:
```cron
0 * * * * cd /home/user/python-pro-labs && /home/user/python-pro-labs/.venv/bin/python src/file_organizer.py /home/user/Downloads
```

Run every 30 minutes:
```cron
*/30 * * * * cd /home/user/python-pro-labs && /home/user/python-pro-labs/.venv/bin/python src/file_organizer.py /home/user/Downloads
```

---

## Logging and Monitoring

### With Python Scheduler

Logs are printed to console. To save logs to a file, redirect output:

```bash
python src/file_organizer_scheduler.py C:\Users\YourName\Downloads daily 09:00 > organizer.log 2>&1
```

### With Windows Task Scheduler

1. Right-click the task and select "Properties"
2. Go to the "Actions" tab
3. Edit the action and check "Create a task with the following properties"
4. Redirect output to a log file by modifying the argument:

```
src\file_organizer.py C:\Users\YourName\Downloads >> C:\logs\organizer.log 2>&1
```

---

## Troubleshooting

### Task doesn't run
- Ensure the Python path is correct
- Check that the directory paths exist
- Verify file permissions for read/write

### Task runs but doesn't organize files
- Check the log file for error messages
- Ensure the directory path is correct
- Verify that files exist in the directory

### Task runs but appears frozen
- The task is likely running in the background (normal)
- Check the target directory to confirm files were organized
- View logs to confirm successful execution

---

## Recommended Schedule

- **Downloads folder**: Daily at 9:00 AM
- **Desktop**: Weekly on Saturday at 10:00 AM
- **Documents**: Weekly on Sunday at 2:00 PM
- **Large folders**: Run hourly every 60 minutes

Choose a schedule that works best for your workflow!
