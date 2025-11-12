"""
================================================================================
Hello World
================================================================================

PURPOSE:
    This is a simple introductory program that demonstrates the basic structure
    of a Python script. It serves as a foundation for learning Python syntax
    and best practices.

KEY FEATURES:
    - Demonstrates the main() function pattern
    - Shows the __name__ == "__main__" idiom
    - Prints a greeting message
    - Follows Python naming conventions and structure

USAGE:
    python hello_world.py

EXPECTED OUTPUT:
    Hello, World!

LEARNING CONCEPTS:
    - Function definition (def)
    - Function calls
    - Print function
    - Script entry point (__main__)
    - Code organization with functions

SCRIPT STRUCTURE:
    1. main() function - Contains the main program logic
    2. Script entry point - Ensures main() runs only when script is executed directly

================================================================================
"""


def main():
    """
    FUNCTION: main
    
    PURPOSE:
        The entry point function that contains the primary program logic.
        This follows the Python best practice of wrapping code in a main()
        function rather than executing code at the module level.
    
    FUNCTIONALITY:
        Prints the greeting "Hello, World!" to the console
    """
    print("Hello, World!")


# ================================================================================
# SCRIPT EXECUTION
# ================================================================================

if __name__ == "__main__":
    """
    Script entry point check.
    
    The condition __name__ == "__main__" is True only when this script is
    run directly. If this script is imported as a module in another script,
    the main() function will not be automatically called.
    
    This allows the script to be both executable and importable.
    """
    main()