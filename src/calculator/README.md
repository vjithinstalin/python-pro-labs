# Simple Calculator

An interactive calculator application that performs basic arithmetic operations with error handling.

**👤 Creator:** [vjithinstalin](https://github.com/vjithinstalin)

---

## 📝 Description

A command-line calculator that demonstrates fundamental programming concepts including:

- Function definitions with parameters and return values
- Interactive user input and output
- Conditional statements and loops
- Error handling and validation
- Code organization and documentation

## 🚀 Running the Program

### From the calculator folder:
```bash
python calculator.py
```

### From the project root:
```bash
python src/calculator/calculator.py
```

## 📊 Interactive Menu

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

Enter choice (1/2/3/4/5): 
```

## 💡 Learning Concepts

This project teaches:

### 1. **Function Definitions**
   - Functions with parameters: `def add(x, y):`
   - Functions with return values
   - Function documentation with docstrings

### 2. **Function Calls**
   - Calling functions with arguments
   - Receiving and using return values

### 3. **Arithmetic Operations**
   - Addition, subtraction, multiplication, division
   - Basic math operations in Python

### 4. **User Input**
   - Getting input with `input()`
   - Converting string input to numbers with `float()`
   - Parsing user choices

### 5. **Loops**
   - While loops for repeated execution
   - Breaking out of loops with `break`

### 6. **Conditionals**
   - If/elif/else statements
   - Multiple condition checking
   - Decision trees

### 7. **Error Handling**
   - try/except blocks
   - Catching ValueError for invalid input
   - Division by zero protection

### 8. **String Formatting**
   - f-strings for formatted output
   - Displaying results clearly

## 🔧 Operations

| Operation | Input | Output |
|-----------|-------|--------|
| Add | 10, 5 | 15.0 |
| Subtract | 10, 3 | 7.0 |
| Multiply | 4, 5 | 20.0 |
| Divide | 20, 4 | 5.0 |
| Divide by Zero | 10, 0 | Error! Division by zero. |

## 📋 Code Structure

```
1. ARITHMETIC FUNCTIONS
   ├── add(x, y)
   ├── subtract(x, y)
   ├── multiply(x, y)
   └── divide(x, y)

2. MAIN PROGRAM
   └── main() - Interactive menu and loop

3. SCRIPT EXECUTION
   └── if __name__ == "__main__"
```

## 🎯 Features

### ✅ Implemented
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division with zero-division protection
- 🔄 Continuous operation (loop until exit)
- ⚠️ Input validation and error handling
- 📊 Clear menu and output formatting

### 💡 Possible Enhancements
- Power operation (x^y)
- Square root calculation
- Percentage calculation
- Operation history/calculator memory
- More advanced error handling
- Input range validation
- Unit conversion
- GUI interface using tkinter

## 📤 Example Session

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

Enter choice (1/2/3/4/5): 4
Enter first number: 20
Enter second number: 4
20.0 / 4.0 = 5.0

Enter choice (1/2/3/4/5): 5
Thank you for using the calculator!
```

## 🔍 Key Functions

### `add(x, y)`
Returns the sum of two numbers.

### `subtract(x, y)`
Returns the difference of two numbers.

### `multiply(x, y)`
Returns the product of two numbers.

### `divide(x, y)`
Returns the quotient with zero-division protection.

### `main()`
- Displays the menu
- Gets user input
- Calls appropriate function
- Displays results
- Handles errors
- Continues until user exits

## 📚 Learning Progression

1. **Basic**: Understand the four arithmetic operations
2. **Intermediate**: Follow the program flow and loops
3. **Advanced**: Study error handling and input validation
4. **Expert**: Extend with new features and improvements

## 🎓 Educational Value

This project is excellent for learning:
- How to build interactive CLI applications
- Proper error handling in production code
- Code organization and documentation
- User experience design for command-line tools
- Debugging strategies

## 🔗 Related Projects

- `../hello_world/` - Start with basic concepts
- `../file_organizer/` - Explore more complex applications

## 📝 Notes

- This program has no external dependencies
- It requires only Python 3.7 or higher
- The program loops continuously until the user chooses to exit
- All inputs are validated and errors are handled gracefully
