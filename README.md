# Python Pro Labs

A collection of Python projects for learning and practice.

## Project Structure

```
python-pro-labs/
│
└── src/
    ├── hello_world.py
    └── calculator.py
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

## Contributing

Feel free to expand these projects with additional features or create new ones!