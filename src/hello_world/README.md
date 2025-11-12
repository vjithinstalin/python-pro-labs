# Hello World

A simple introductory program that demonstrates basic Python syntax and structure.

**👤 Creator:** [vjithinstalin](https://github.com/vjithinstalin)

---

## 📝 Description

This is a beginner-friendly program that prints "Hello, World!" to the console. It demonstrates fundamental Python concepts including:

- Function definition and calling
- The `print()` function
- Script entry point with `if __name__ == "__main__"`
- Code organization best practices

## 🚀 Running the Program

### From the hello_world folder:
```bash
python hello_world.py
```

### From the project root:
```bash
python src/hello_world/hello_world.py
```

## 📤 Expected Output

```
Hello, World!
```

## 💡 Learning Concepts

This project teaches:

1. **Function Definition**
   - How to define a function with `def`
   - Function documentation with docstrings

2. **Function Calls**
   - How to call a function from within the script
   - Return values (implicit None in this case)

3. **Print Function**
   - Basic output to console
   - String literals

4. **Script Entry Point**
   - The `__name__` special variable
   - The `if __name__ == "__main__"` pattern
   - Running code only when script is executed directly

5. **Code Organization**
   - Wrapping logic in functions
   - Following Python conventions
   - Writing clear, readable code

## 🔍 Code Structure

```python
def main():
    # Main program logic
    print("Hello, World!")

if __name__ == "__main__":
    # Entry point - runs only when script is executed directly
    main()
```

## 📚 Next Steps

After understanding this basic program, you can:

1. Modify the message (e.g., print your name)
2. Add more functions to perform different tasks
3. Learn about command-line arguments
4. Explore the `calculator.py` for more complex logic

## 🎯 Key Takeaways

- **Main Function Pattern**: Good practice to wrap code in a `main()` function
- **Entry Point Check**: Always use `if __name__ == "__main__"` for scripts
- **Readability**: Well-organized code is easier to understand and maintain
- **Documentation**: Comments and docstrings help explain code purpose

## 📝 Notes

- This program has no external dependencies
- It requires only Python 3.7 or higher
- The script is fully self-contained and cross-platform compatible

## 🔗 Related Projects

- `../calculator/` - Learn about functions with parameters
- `../file_organizer/` - Explore more complex real-world applications
