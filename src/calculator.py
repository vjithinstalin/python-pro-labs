"""
================================================================================
Simple Calculator
================================================================================

PURPOSE:
    An interactive calculator application that performs basic arithmetic
    operations. This project demonstrates how to build an interactive CLI
    application with functions, loops, conditionals, and error handling.

KEY FEATURES:
    - Interactive menu-driven interface
    - Basic arithmetic operations (add, subtract, multiply, divide)
    - Error handling for invalid inputs and division by zero
    - Clear user prompts and formatted output
    - Graceful exit mechanism

USAGE:
    python calculator.py

EXPECTED WORKFLOW:
    1. Display main menu
    2. Prompt user to select an operation
    3. Get two numbers from user
    4. Perform calculation
    5. Display result
    6. Repeat until user chooses to exit

LEARNING CONCEPTS:
    - Function definitions with parameters and return values
    - Function documentation and docstrings
    - While loops for program flow
    - Conditional statements (if/elif/else)
    - Error handling with try/except
    - User input with input()
    - String formatting and f-strings
    - Code organization with functions

SCRIPT STRUCTURE:
    1. ARITHMETIC FUNCTIONS (add, subtract, multiply, divide)
    2. MAIN FUNCTION (Interactive menu and program loop)
    3. SCRIPT EXECUTION (Entry point)

================================================================================
"""


# ================================================================================
# SECTION 1: ARITHMETIC FUNCTIONS
# ================================================================================

def add(x, y):
    """
    FUNCTION: add
    
    PURPOSE:
        Adds two numbers together.
    
    PARAMETERS:
        x (float/int): First number
        y (float/int): Second number
    
    RETURNS:
        float/int: The sum of x and y
    
    EXAMPLE:
        >>> add(5, 3)
        8
    """
    return x + y


def subtract(x, y):
    """
    FUNCTION: subtract
    
    PURPOSE:
        Subtracts the second number from the first.
    
    PARAMETERS:
        x (float/int): First number (minuend)
        y (float/int): Second number (subtrahend)
    
    RETURNS:
        float/int: The difference (x - y)
    
    EXAMPLE:
        >>> subtract(10, 3)
        7
    """
    return x - y


def multiply(x, y):
    """
    FUNCTION: multiply
    
    PURPOSE:
        Multiplies two numbers together.
    
    PARAMETERS:
        x (float/int): First number
        y (float/int): Second number
    
    RETURNS:
        float/int: The product of x and y
    
    EXAMPLE:
        >>> multiply(4, 5)
        20
    """
    return x * y


def divide(x, y):
    """
    FUNCTION: divide
    
    PURPOSE:
        Divides the first number by the second with zero-division protection.
    
    PARAMETERS:
        x (float/int): First number (dividend)
        y (float/int): Second number (divisor)
    
    RETURNS:
        float/int or str: The quotient (x / y), or error message if y is 0
    
    ERROR HANDLING:
        Returns "Error! Division by zero." if y is 0
    
    EXAMPLE:
        >>> divide(20, 4)
        5.0
        >>> divide(10, 0)
        'Error! Division by zero.'
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y


# ================================================================================
# SECTION 2: MAIN PROGRAM
# ================================================================================

def main():
    """
    FUNCTION: main
    
    PURPOSE:
        Entry point for the calculator. Displays an interactive menu and handles
        the main program loop for user interactions.
    
    FUNCTIONALITY:
        1. Displays calculator menu with operation choices
        2. Prompts user to select an operation (1-5)
        3. For valid operations (1-4):
           - Gets two numbers from user
           - Performs the calculation
           - Displays the result
        4. For option 5: Exits the program
        5. Continues looping until user chooses to exit
    
    ERROR HANDLING:
        - Catches ValueError if non-numeric input is provided
        - Validates operation choice and rejects invalid selections
        - Displays user-friendly error messages
    """
    print("Simple Calculator")
    print("-" * 40)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-" * 40)
    
    # MAIN LOOP - Continues until user chooses to exit (option 5)
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        # EXIT CONDITION
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        # OPERATION SELECTION AND EXECUTION
        if choice in ('1', '2', '3', '4'):
            try:
                # GET USER INPUT
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # PERFORM CALCULATION AND DISPLAY RESULT
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
            except ValueError:
                # ERROR HANDLING - Invalid numeric input
                print("Invalid input! Please enter numeric values.")
        else:
            # ERROR HANDLING - Invalid choice selection
            print("Invalid choice! Please select a valid operation.")


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
