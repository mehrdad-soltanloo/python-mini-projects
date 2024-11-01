# Even/Odd List Splitter

## Introduction

The Even/Odd List Splitter is a simple command-line Python application that takes a list of numbers from the user, separates them into even and odd numbers, and displays the results. This guide will walk you through the entire codebase, explaining each line and function as though you're learning chapter-by-chapter in a book.

## Getting Started

### Prerequisites

To run this app, you only need Python installed on your system. The code is compatible with Python 3 and can be run directly from the command line.

### Running the App

To execute this script from the command line:

1. Clone this repository or copy the `splitter.py` file into a directory.
2. Run the file with:

```bash
   python splitter.py
```

Alternatively, you can make the script executable as shown below.

### Making It CLI Executable

To make this script run directly from the terminal, follow these steps:

Add a shebang line at the top of the script:

```python
#!/usr/bin/env python3
```

This tells the terminal to use Python to interpret the script.

### Make the script executable:

```bash
chmod +x splitter.py
```

Now you can run it from the current directory as:

```bash
./splitter.py
```

(Optional): To make it accessible from anywhere on your system, move it to a directory in your PATH, such as `/usr/local/bin`:

```bash
sudo mv splitter.py /usr/local/bin/splitter
```

Now, run it with:

```bash
splitter
```

## Code Walkthrough

### Code Structure

The code follows a typical modular approach. Here’s an overview of the structure:

```python
#!/usr/bin/env python3    # Shebang for CLI execution

def main():               # Main function to encapsulate the app logic
    user_input = input("Enter a list of numbers separated by spaces: ")

    # Convert input to list of integers
    numbers_list = list(map(int, user_input.split()))

    # Separate even and odd numbers using list comprehensions
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    odd_numbers = [num for num in numbers_list if num % 2 != 0]

    # Display the results
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

# This block ensures main() runs only when this script is executed directly
if __name__ == "__main__":
    main()
```

---

### Detailed Explanation

1. **The Shebang Line**

   ```python
   #!/usr/bin/env python3
   ```

   This line allows the script to be executed directly as a command line (CLI) executable by using the system’s Python interpreter. It makes the script self-contained and easily runnable.

2. **Defining the `main()` Function**

   ```python
   def main():
   ```

   We define `main()` to encapsulate the core functionality of our app. Using a `main()` function is a best practice in Python, as it organizes code, making it reusable and maintainable.

3. **User Input with `input()`**

   ```python
   user_input = input("Enter a list of numbers separated by spaces: ")
   ```

   This line prompts the user to enter numbers. `input()` captures the user input as a string. We specifically ask for numbers separated by spaces for easy parsing.

4. **Parsing and Converting Input to Integers**

   ```python
   numbers_list = list(map(int, user_input.split()))
   ```

   - `user_input.split()`: `split()` breaks the input string into a list of individual number strings based on spaces. For example, if the user enters "3 5 6", it becomes `['3', '5', '6']`.
   - `map(int, ...)`: `map()` applies the `int` function to each item in the list, converting each string to an integer.
   - `list(...)`: Wrapping `map()` in `list()` ensures `numbers_list` can be used multiple times, which wouldn’t be possible if it remained as a map iterator.

5. **Separating Even and Odd Numbers with List Comprehensions**

   ```python
   even_numbers = [num for num in numbers_list if num % 2 == 0]
   odd_numbers = [num for num in numbers_list if num % 2 != 0]
   ```

   - **List Comprehensions**: Here, list comprehensions offer a concise way to create `even_numbers` and `odd_numbers` lists. Using conditions inside list comprehensions is both readable and efficient.
   - **Modulo Operator %**: We use `num % 2 == 0` to check if a number is even. The modulo operator returns the remainder of `num` divided by 2. If the remainder is zero, the number is even; otherwise, it’s odd.

6. **Displaying Results**

   ```python
   print("Even numbers:", even_numbers)
   print("Odd numbers:", odd_numbers)
   ```

   - `print()`: The `print()` function displays `even_numbers` and `odd_numbers` lists in a user-friendly format, helping users clearly see the separation of numbers.

7. **Conditional Entry Point**
   ```python
   if __name__ == "__main__":
       main()
   ```
   This line ensures that `main()` only runs if the script is executed directly. If imported as a module, `main()` won’t run automatically. This setup is useful if the app grows or if we want to import functions from this file into other scripts.

---

## Example Usage

### Running the Script

Run the script as follows:

```bash
python splitter.py
```

**User Input**: The app prompts:

```plaintext
Enter a list of numbers separated by spaces:
```

**Example input**:

```plaintext
2 3 5 8 10
```

**Output**:

```plaintext
Even numbers: [2, 8, 10]
Odd numbers: [3, 5]
```

---

## Conclusion

This Even/Odd List Splitter is a simple yet effective Python script, demonstrating foundational programming concepts such as user input, list manipulation, and conditional logic. The code is well-structured, modular, and follows best practices, making it a great foundation for more complex projects.

---

## Files and Folders

### Folder Structure

The folder structure for this project:

```bash
even_odd_splitter/
│
├── splitter.py            # Main script file
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

### .gitignore Example

To ignore unnecessary files in Git, here’s a basic `.gitignore` setup:

```plaintext
# Ignore the virtual environment
venv/

# Ignore Python cache files
__pycache__/
*.pyc

# Ignore environment and editor files
.env
*.env
.idea/
.vscode/

# Ignore OS-generated files
.DS_Store
Thumbs.db
```

> Thank you for checking out splitter ap! I appreciate your time and interest in this project. Whether you're using the app, providing feedback, or contributing to the code, your support means a lot. I hope you find this project useful and inspiring for your own development journey.

Happy coding! 🙂
