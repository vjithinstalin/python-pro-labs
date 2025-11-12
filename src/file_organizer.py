import os
import shutil
from pathlib import Path
from collections import defaultdict

# Define file type categories and their extensions
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

def get_file_category(file_extension):
    """Determine the category of a file based on its extension"""
    file_extension = file_extension.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    return 'Other'

def organize_files(directory_path):
    """Organize files in the given directory into folders by type"""
    
    # Validate directory path
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return False
    
    organized_count = 0
    skipped_count = 0
    error_count = 0
    
    print(f"\n{'='*60}")
    print(f"File Organizer - Organizing: {directory_path}")
    print(f"{'='*60}\n")
    
    # Get all files in the directory (excluding subdirectories)
    try:
        items = os.listdir(directory_path)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'")
        return False
    
    # Statistics
    stats = defaultdict(int)
    
    for item in items:
        item_path = os.path.join(directory_path, item)
        
        # Skip directories and hidden files
        if os.path.isdir(item_path) or item.startswith('.'):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(item)
        
        if not file_extension:
            skipped_count += 1
            continue
        
        # Determine category
        category = get_file_category(file_extension)
        stats[category] += 1
        
        # Create category folder if it doesn't exist
        category_folder = os.path.join(directory_path, category)
        if not os.path.exists(category_folder):
            try:
                os.makedirs(category_folder)
                print(f"✓ Created folder: {category}")
            except Exception as e:
                print(f"✗ Error creating folder '{category}': {e}")
                error_count += 1
                continue
        
        # Move file to category folder
        destination = os.path.join(category_folder, item)
        
        # Handle file name conflicts
        if os.path.exists(destination):
            name, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(os.path.join(category_folder, f"{name}_{counter}{ext}")):
                counter += 1
            destination = os.path.join(category_folder, f"{name}_{counter}{ext}")
            item = f"{name}_{counter}{ext}"
        
        try:
            shutil.move(item_path, destination)
            print(f"→ Moved: {item} → {category}/")
            organized_count += 1
        except Exception as e:
            print(f"✗ Error moving '{item}': {e}")
            error_count += 1
    
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

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <directory_path>")
        print("\nExample:")
        print("  python file_organizer.py C:\\Users\\YourName\\Downloads")
        print("  python file_organizer.py /home/user/documents")
        sys.exit(1)
    
    directory = sys.argv[1]
    organize_files(directory)

if __name__ == "__main__":
    main()
