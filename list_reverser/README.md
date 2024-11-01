# CLI List Manipulator

A Python-based command-line interface (CLI) tool for performing various operations on a list of numbers. The tool allows users to reverse, sort, remove duplicates, filter even/odd numbers, and save the modified list to a file.

## Features

- Reverse the list.
- Sort the list in ascending or descending order.
- Remove duplicates while preserving the original order.
- Filter even or odd numbers.
- Save the modified list to a file.

## Prerequisites

- Python 3.x installed on your machine.

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/mehrdad-soltanloo/python-cli-list-manipulator.git
   ```

## Usage

To run the script:

```bash
python list_manipulator.py
```

### Algorithm

1. Take user input to provide a list or use a default list.
2. Display a menu of operations:

- Reverse the list.
- Sort the list.
- Remove duplicates.
- Filter even or odd numbers.
- Save the list to a file.

3. Process the user's choice and apply the corresponding function to the list.
4. Display the modified list after each operation.
5. Repeat until the user selects the exit option.

### Step-by-Step Guide

- Input Handling: The program asks the user to either input a list manually or use a predefined list. If the user provides input, it splits the numbers into a list of integers.
- Menu Display: A menu is shown to the user, providing options to manipulate the list.
- Reverse the List: If chosen, the list is reversed using the reverse_list() function.
- Sort the List: The user selects ascending or descending sort, and the list is sorted accordingly.
- Remove Duplicates: Duplicates are removed from the list while maintaining the original order.
- Filter Even or Odd Numbers: The user can filter only even or odd numbers from the list.
- Save the List to a File: The user can save the modified list to a text file.

### Functions Explained

**get_user_list()**

- Purpose: To get the list of numbers from the user or use a default list.
- Why it's used: Allows flexibility for the user to input a list of their choice or fall back to a default list for testing.

**display_menu()**

- Purpose: Displays the available operations for the user.
- Why it's used: Keeps the interface user-friendly by clearly showing available options at each step.

**reverse_list(numbers)**

- Purpose: Reverses the order of the list in place.
- Why it's used: List reversal is a common list operation, and it demonstrates how in-place modifications can be done efficiently using the reverse() method.

**sort_list(numbers)**

- Purpose: Sorts the list either in ascending or descending order.
- Why it's used: Sorting is another common operation. The sorted() function allows sorting without altering the original list unless assigned back.

**remove_duplicates(numbers)**

- Purpose: Removes duplicates from the list while maintaining the original order.
- Why it's used: Python’s dict.fromkeys() is a neat trick to remove duplicates while maintaining the original insertion order.

**filter_list(numbers, even=True)**

- Purpose: Filters the list to return either even or odd numbers.
- Why it's used: Demonstrates the use of list comprehensions to perform filtering based on conditions.

**save_to_file(numbers)**

- Purpose: Saves the modified list to a text file.
- Why it's used: Demonstrates file handling in Python by writing data to a file, ensuring results are preserved outside the program.

**main()**

- Purpose: The main loop that handles user input and directs them to the appropriate list manipulation functions.
- Why it's used: Centralizes the logic of the program, ensuring each part of the project interacts correctly.

> Thank you for checking out this project! Your interest and contributions are highly appreciated. If you have any questions or feedback, don't hesitate to reach out or open an issue on GitHub. Happy coding! 🙂
