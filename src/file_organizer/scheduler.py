"""
================================================================================
File Organizer Scheduler
================================================================================

PURPOSE:
    This script provides automated scheduling capabilities for the organizer.py
    script. It allows users to automatically organize files in a specified directory
    at regular intervals (hourly, daily, or weekly).

KEY FEATURES:
    - Schedule file organization at custom intervals
    - Support for multiple frequency options (hourly, daily, weekly)
    - Timestamped logging of each operation
    - Cross-platform compatibility (Windows, macOS, Linux)
    - Error handling and status reporting
    - Graceful shutdown with Ctrl+C

USAGE:
    python scheduler.py <directory_path> [frequency] [time]
    
EXAMPLES:
    # Run every day at 9:00 AM
    python scheduler.py C:\\Users\\YourName\\Downloads daily 09:00
    
    # Run every 60 minutes
    python scheduler.py C:\\Users\\YourName\\Downloads hourly 60
    
    # Run every Monday at 10:00 AM
    python scheduler.py C:\\Users\\YourName\\Downloads weekly monday 10:00

SCRIPT STRUCTURE:
    1. IMPORTS & SETUP
       - Imports necessary libraries for scheduling and subprocess execution
    
    2. CORE FUNCTIONS
       - run_file_organizer(): Executes the organizer process
       - schedule_organizer(): Configures and starts the scheduler
       - main(): Parses command-line arguments and initializes the scheduler
    
    3. SCHEDULING LOGIC
       - Supports hourly, daily, and weekly scheduling
       - Uses the 'schedule' library for reliable task scheduling
       - Validates user input and provides helpful error messages
    
    4. EXECUTION & LOGGING
       - Runs scheduled tasks with timestamp logging
       - Captures and displays output from file organizer
       - Handles exceptions and provides error feedback

================================================================================
"""

import schedule
import time
import subprocess
import sys
from datetime import datetime

# ================================================================================
# SECTION 1: CORE FUNCTIONS
# ================================================================================

def run_file_organizer(directory_path):
    """
    FUNCTION: run_file_organizer
    
    PURPOSE:
        Executes the organizer.py script as a subprocess for the specified
        directory. Captures and logs the output with timestamps.
    
    PARAMETERS:
        directory_path (str): The full path to the directory to organize
    
    FUNCTIONALITY:
        1. Prints timestamp and directory being organized
        2. Runs organizer.py as a subprocess
        3. Captures stdout and stderr
        4. Checks return code for success/failure
        5. Logs output and any errors with timestamps
    
    ERROR HANDLING:
        - Catches and logs any exceptions during execution
        - Reports errors without stopping the scheduler
    """
    try:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running file organizer for: {directory_path}")
        result = subprocess.run(
            [sys.executable, "organizer.py", directory_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✓ File organizer completed successfully")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✗ Error running file organizer")
            if result.stderr:
                print(result.stderr)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✗ Exception occurred: {e}")

# ================================================================================
# SECTION 2: SCHEDULING CONFIGURATION
# ================================================================================

def schedule_organizer(directory_path, frequency='daily', time_str='09:00'):
    """
    FUNCTION: schedule_organizer
    
    PURPOSE:
        Configures the scheduler based on frequency preference and starts the
        continuous scheduling loop. This is the heart of the scheduler that sets
        up when and how often tasks should run.
    
    PARAMETERS:
        directory_path (str): Path to the directory to organize
        frequency (str): How often to run - 'hourly', 'daily', or 'weekly'
        time_str (str): Time details depending on frequency:
                       - For hourly: minutes (e.g., '60')
                       - For daily: time in HH:MM format (e.g., '09:00')
                       - For weekly: day and time (e.g., 'monday 10:00')
    
    RETURNS:
        bool: True if scheduler started successfully, False otherwise
    
    SCHEDULING MODES:
        1. HOURLY: Runs every N minutes (specify interval in time_str)
        2. DAILY: Runs every day at specified time (HH:MM format)
        3. WEEKLY: Runs on specific day at specific time
    
    FUNCTIONALITY:
        1. Validates user input and frequency type
        2. Configures the appropriate schedule based on frequency
        3. Enters infinite loop to check and run pending tasks
        4. Sleeps for 1 second between each check (minimal CPU usage)
        5. Handles Ctrl+C gracefully for clean shutdown
    
    DAY MAPPING (for weekly):
        monday, tuesday, wednesday, thursday, friday, saturday, sunday
    """
    
    # Display scheduler configuration
    print(f"{'='*60}")
    print(f"File Organizer Scheduler")
    print(f"{'='*60}")
    print(f"Directory: {directory_path}")
    print(f"Frequency: {frequency}")
    print(f"Time: {time_str}")
    print(f"{'='*60}\n")
    
    # ====================================================================
    # SCHEDULE CONFIGURATION LOGIC
    # ====================================================================
    
    if frequency.lower() == 'hourly':
        # HOURLY SCHEDULING
        # Extracts interval from time_str, defaults to 60 minutes if invalid
        interval = int(time_str) if time_str.isdigit() else 60
        schedule.every(interval).minutes.do(run_file_organizer, directory_path)
        print(f"✓ Scheduled to run every {interval} minute(s)")
    
    elif frequency.lower() == 'daily':
        # DAILY SCHEDULING
        # Schedules task to run at specific time each day (HH:MM format)
        schedule.every().day.at(time_str).do(run_file_organizer, directory_path)
        print(f"✓ Scheduled to run daily at {time_str}")
    
    elif frequency.lower() == 'weekly':
        # WEEKLY SCHEDULING
        # Extracts day name and time from time_str parameter
        # Format expected: "monday 10:00" or "tuesday 14:30", etc.
        day = time_str.split()[0].lower() if ' ' in time_str else 'monday'
        time_part = time_str.split()[1] if ' ' in time_str else '09:00'
        
        # Map day names to schedule library functions
        day_mapping = {
            'monday': schedule.every().monday,
            'tuesday': schedule.every().tuesday,
            'wednesday': schedule.every().wednesday,
            'thursday': schedule.every().thursday,
            'friday': schedule.every().friday,
            'saturday': schedule.every().saturday,
            'sunday': schedule.every().sunday,
        }
        
        if day in day_mapping:
            day_mapping[day].at(time_part).do(run_file_organizer, directory_path)
            print(f"✓ Scheduled to run every {day} at {time_part}")
        else:
            print(f"✗ Invalid day: {day}")
            return False
    
    else:
        # INVALID FREQUENCY ERROR
        print(f"✗ Invalid frequency: {frequency}")
        return False
    
    # ====================================================================
    # SCHEDULER MAIN LOOP
    # Continuously checks for scheduled tasks and executes them
    # ====================================================================
    
    print("\nScheduler is running. Press Ctrl+C to stop.\n")
    
    # Keep the scheduler running
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Scheduler stopped by user")

# ================================================================================
# SECTION 3: ARGUMENT PARSING & INITIALIZATION
# ================================================================================

def main():
    """
    FUNCTION: main
    
    PURPOSE:
        Entry point for the script. Parses command-line arguments and initializes
        the scheduler with user-provided parameters.
    
    COMMAND-LINE ARGUMENTS:
        1. directory_path (required): The directory to organize
        2. frequency (optional): 'hourly', 'daily', or 'weekly' (default: 'daily')
        3. time (optional): Time specification:
                           - For hourly: minutes (default: '60')
                           - For daily: HH:MM format (default: '09:00')
                           - For weekly: day and HH:MM (default: 'monday 09:00')
    
    FUNCTIONALITY:
        1. Checks if minimum arguments are provided
        2. Displays usage examples if missing arguments
        3. Parses command-line arguments with defaults
        4. Handles special case for weekly scheduling (day + time)
        5. Calls schedule_organizer() to start the scheduler
    """
    if len(sys.argv) < 2:
        # DISPLAY USAGE INFORMATION
        # Shows examples and detailed information about how to use the script
        print("Usage: python scheduler.py <directory_path> [frequency] [time]")
        print("\nExamples:")
        print("  # Run every day at 9:00 AM")
        print("  python scheduler.py C:\\Users\\YourName\\Downloads daily 09:00")
        print("\n  # Run every hour")
        print("  python scheduler.py C:\\Users\\YourName\\Downloads hourly 60")
        print("\n  # Run every Monday at 10:00 AM")
        print("  python scheduler.py C:\\Users\\YourName\\Downloads weekly monday 10:00")
        print("\nFrequency options:")
        print("  - hourly <minutes>: Run every N minutes (default: 60)")
        print("  - daily <HH:MM>: Run daily at specified time (default: 09:00)")
        print("  - weekly <day> <HH:MM>: Run on specified day at time (default: monday 09:00)")
        sys.exit(1)
    
    # PARSE COMMAND-LINE ARGUMENTS
    # Extract directory and optional frequency/time parameters
    directory = sys.argv[1]
    frequency = sys.argv[2].lower() if len(sys.argv) > 2 else 'daily'
    time_str = sys.argv[3] if len(sys.argv) > 3 else ('09:00' if frequency != 'hourly' else '60')
    
    # Handle weekly scheduling with day and time as separate arguments
    if frequency == 'weekly' and len(sys.argv) > 4:
        time_str = f"{sys.argv[3]} {sys.argv[4]}"
    
    # START THE SCHEDULER
    schedule_organizer(directory, frequency, time_str)

# ================================================================================
# SCRIPT EXECUTION
# ================================================================================

if __name__ == "__main__":
    main()
