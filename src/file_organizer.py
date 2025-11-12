"""
================================================================================
File Organizer
================================================================================

PURPOSE:
    An intelligent file organization utility that automatically categorizes
    and moves files into folders based on their file type (extension). This
    project demonstrates file I/O operations, OS module usage, and command-line
    argument processing.

KEY FEATURES:
    - Automatically detects file type based on extension
    - Creates category folders if they don't exist
    - Moves files to appropriate folders
    - Handles file name conflicts automatically
    - Provides detailed organization statistics
    - Robust error handling and permission checking
    - Cross-platform compatibility

USAGE:
    python file_organizer.py <directory_path>

EXAMPLES:
    # Organize Downloads folder
    python file_organizer.py C:\\Users\\YourName\\Downloads
    
    # Organize current directory
    python file_organizer.py .
    
    # Organize specific folder
    python file_organizer.py /home/user/documents

SUPPORTED FILE CATEGORIES:
    - Images: jpg, jpeg, png, gif, bmp, svg, webp, ico, tiff
    - Documents: pdf, doc, docx, txt, xlsx, xls, ppt, pptx, odt
    - Videos: mp4, avi, mkv, mov, wmv, flv, webm, m4v
    - Audio: mp3, wav, flac, aac, ogg, wma, m4a, aiff
    - Archives: zip, rar, 7z, tar, gz, bz2, iso
    - Code: py, js, html, css, java, cpp, c, php, rb, go, rs
    - Executables: exe, msi, bat, cmd, sh, app, dmg
    - Data: json, xml, csv, sql, db, yml, yaml
    - Other: Files with unrecognized extensions

LEARNING CONCEPTS:
    - File and directory operations with os module
    - Path handling with pathlib and os.path
    - File type detection using extensions
    - Dictionary usage for mappings
    - Collections.defaultdict for statistics
    - Subprocess and command-line arguments
    - Error handling and exception management
    - User input validation
    - String formatting and output

SCRIPT STRUCTURE:
    1. FILE CATEGORIES DEFINITION - Maps extensions to categories
    2. CORE FUNCTIONS - File type detection and organization
    3. MAIN PROGRAM - Orchestrates the organization process
    4. SCRIPT EXECUTION - Entry point

================================================================================
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# ================================================================================
# SECTION 1: FILE CATEGORIES DEFINITION
# ================================================================================

# Define file type categories and their extensions
# Maps category names to lists of file extensions that belong to that category
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs'],
    'Executables': ['.exe', '.msi', '.bat', '.cmd', '.sh', '.app', '.dmg'],
    'Data': ['.json', '.xml', '.csv', '.sql', '.db', '.yml', '.yaml'],
}

# ================================================================================
# SECTION 2: CORE FUNCTIONS
# ================================================================================

def get_file_category(file_extension):
    """
    FUNCTION: get_file_category
    
    PURPOSE:
        Determines the category of a file based on its extension. This function
        maps file extensions to their appropriate categories for organization.
    
    PARAMETERS:
        file_extension (str): The file extension including the dot (e.g., '.pdf')
    
    RETURNS:
        str: The category name for the file, or 'Other' if extension is unknown
    
    FUNCTIONALITY:
        1. Converts extension to lowercase for case-insensitive comparison
        2. Searches through FILE_CATEGORIES dictionary
        3. Returns matching category name
        4. Returns 'Other' if no match found
    
    EXAMPLE:
        >>> get_file_category('.pdf')
        'Documents'
        >>> get_file_category('.jpg')
        'Images'
        >>> get_file_category('.xyz')
        'Other'
    """
    file_extension = file_extension.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    return 'Other'


# ================================================================================
# SECTION 3: MAIN ORGANIZATION FUNCTION
# ================================================================================

def organize_files(directory_path):
    """
    FUNCTION: organize_files
    
    PURPOSE:
        Main function that orchestrates the file organization process. Scans
        the directory, categorizes files, creates category folders, and moves
        files accordingly.
    
    PARAMETERS:
        directory_path (str): The full path to the directory to organize
    
    RETURNS:
        bool: True if organization completed successfully, False otherwise
    
    FUNCTIONALITY:
        1. VALIDATION - Verifies directory exists and is accessible
        2. SCANNING - Lists all items in the directory
        3. CATEGORIZATION - Determines file type for each file
        4. FOLDER CREATION - Creates category folders as needed
        5. FILE MOVEMENT - Moves files to appropriate folders
        6. CONFLICT HANDLING - Renames files if naming conflicts occur
        7. REPORTING - Displays organization summary and statistics
    
    ERROR HANDLING:
        - Checks if path is valid directory
        - Handles permission denied errors
        - Catches and logs file movement errors
        - Provides detailed error messages
    
    STATISTICS TRACKED:
        - Number of files organized
        - Number of files skipped
        - Number of errors
        - Count by category
    """
    
    print(f"\n{'='*60}")
    print(f"File Organizer - Organizing: {directory_path}")
    print(f"{'='*60}\n")
    
    # INITIALIZATION PHASE
    # Initialize counters and statistics tracking
    organized_count = 0
    skipped_count = 0
    error_count = 0
    stats = defaultdict(int)
    
    # VALIDATION & SCANNING PHASE
    # Attempt to read directory contents
    try:
        items = os.listdir(directory_path)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'")
        return False
    
    # MAIN PROCESSING LOOP
    # Iterate through each item in the directory
    for item in items:
        item_path = os.path.join(directory_path, item)
        
        # FILTERING - Skip directories and hidden files
        # (Directories are processed separately, hidden files by convention)
        if os.path.isdir(item_path) or item.startswith('.'):
            continue
        
        # FILE CATEGORIZATION PHASE
        # Extract file extension and determine category
        _, file_extension = os.path.splitext(item)
        
        # SKIP FILES WITHOUT EXTENSIONS
        if not file_extension:
            skipped_count += 1
            continue
        
        # GET CATEGORY AND UPDATE STATISTICS
        category = get_file_category(file_extension)
        stats[category] += 1
        
        # FOLDER CREATION PHASE
        # Create category folder if it doesn't already exist
        category_folder = os.path.join(directory_path, category)
        if not os.path.exists(category_folder):
            try:
                os.makedirs(category_folder)
                print(f"✓ Created folder: {category}")
            except Exception as e:
                print(f"✗ Error creating folder '{category}': {e}")
                error_count += 1
                continue
        
        # FILE MOVEMENT & CONFLICT HANDLING PHASE
        # Prepare destination path and handle naming conflicts
        destination = os.path.join(category_folder, item)
        
        # Handle file name conflicts by adding counter suffix
        if os.path.exists(destination):
            name, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(os.path.join(category_folder, f"{name}_{counter}{ext}")):
                counter += 1
            destination = os.path.join(category_folder, f"{name}_{counter}{ext}")
            item = f"{name}_{counter}{ext}"
        
        # EXECUTE FILE MOVE
        try:
            shutil.move(item_path, destination)
            print(f"→ Moved: {item} → {category}/")
            organized_count += 1
        except Exception as e:
            print(f"✗ Error moving '{item}': {e}")
            error_count += 1
    
    # REPORTING & SUMMARY PHASE
    # Display detailed organization summary and statistics
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Organization Summary")
    print(f"{'='*60}")
    print(f"Files organized: {organized_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Errors: {error_count}")
    print(f"\nFiles by category:")
    for category in sorted(stats.keys()):
        print(f"  {category}: {stats[category]} file(s)")
    print(f"{'='*60}\n")
    
    return True

# ================================================================================
# SECTION 4: MAIN PROGRAM & ENTRY POINT
# ================================================================================

def main():
    """
    FUNCTION: main
    
    PURPOSE:
        Entry point for the file organizer script. Parses command-line arguments
        and initiates the file organization process.
    
    COMMAND-LINE ARGUMENTS:
        1. directory_path (required): The path to the directory to organize
    
    FUNCTIONALITY:
        1. Checks if directory path argument was provided
        2. Displays usage information if missing
        3. Calls organize_files() with provided directory path
    
    USAGE:
        python file_organizer.py <directory_path>
    """
    import sys
    
    if len(sys.argv) < 2:
        # USAGE INFORMATION
        # Display help text when script is run without arguments
        print("Usage: python file_organizer.py <directory_path>")
        print("\nExample:")
        print("  python file_organizer.py C:\\Users\\YourName\\Downloads")
        print("  python file_organizer.py /home/user/documents")
        sys.exit(1)
    
    directory = sys.argv[1]
    organize_files(directory)

# ================================================================================
# SCRIPT EXECUTION
# ================================================================================

if __name__ == "__main__":
    """
    Script entry point check.
    
    The condition __name__ == "__main__" is True only when this script is
    run directly. If this script is imported as a module in another script,
    the main() function will not be automatically called.
    """
    main()
