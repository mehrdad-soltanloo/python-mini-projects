# List Sum Calculator

This is a Python command-line tool that prompts the user to enter a list of numbers separated by spaces, calculates the sum of these numbers, and displays the result. After each calculation, the program gives the option to continue with a new set of numbers or exit. This README explains the code’s functionality, why each part is used, and additional project details.

---

## Code Explanation

```python
def main():
    while True:
        # Get user input
        nums = input("Enter numbers separated by spaces: ").split()

        # Check if the input is empty
        if not nums:
            print("No numbers entered")
            continue #Go back to start of the loop

        # Try to convert the input into a list of integers
        try:
            numbers_list = [int(num) for num in nums]
        except ValueError:
            print("Invalid input! Please enter only numbers.")
            continue  # Go back to start of the loop if input is invalid

        # calculate the total sum of the numbers in the created list
        result = sum(numbers_list)

        # Display the result
        print("The sum of the given numbers is: ", result)

        # Ask if the user want to continue with new set of number or exit
        next_mov = input("Do you want to enter more numbers? (yes/no): ").strip().lower()
        if next_mov != 'yes':
            print("See you again!")
            break

if __name__ == "__main__":
    main()
```

## Explanation of Code

The code is structured to provide a looped command-line interface, allowing the user to calculate the sum of lists of numbers multiple times.

### Function Definitions and Code Structure

- def main():: Defines the main() function, which contains the core logic of the program. By encapsulating the code in a function, we ensure that it runs in a structured, reusable way. Using a main() function is a Python best practice, especially for scripts meant to be executed as standalone programs.

- while True:: This initiates an infinite loop, allowing the program to continuously prompt the user for new inputs until they choose to exit. Using an infinite loop here enables repeated calculations without restarting the program.

### Step-by-Step Code Explanation

1. User Input:

```python
nums = input("Enter numbers separated by spaces: ").split()
```

- Explanation: This line prompts the user to enter numbers separated by spaces and uses .split() to split the input into a list of strings (e.g., ["1", "2", "3"]).
- Why Use .split()?: Splitting the input allows us to handle each number individually and prepare it for conversion into integers.

2. Input Validation:

```python
if not nums:
print("No numbers entered")
continue
```

- Explanation: Checks if nums is empty. If the user presses Enter without typing anything, the program informs them that no numbers were entered and restarts the loop.
- Why Validate Input?: This prevents errors that could arise from trying to process empty input, improving the program's reliability and user experience.

3. Error Handling with try...except:

```python
try:
numbers_list = [int(num) for num in nums]
except ValueError:
print("Invalid input! Please enter only numbers.")
continue
```

- Explanation: This try...except block attempts to convert each element in nums into an integer, storing them in numbers_list. If any element cannot be converted (e.g., a non-numeric input like "abc"), a ValueError is raised. The except block catches this error, displays an error message, and restarts the loop.
- Why Use try...except?: The try...except block allows the program to handle incorrect input gracefully, preventing it from crashing due to invalid entries.

4. Calculating the Sum:

```python
result = sum(numbers_list)
```

- Explanation: This line uses Python’s built-in sum() function to calculate the total of all integers in numbers_list.
- Why Use sum()?: sum() provides a straightforward way to add up list items, making the code concise and readable.

5. Displaying the Result:

```python
print("The sum of the given numbers is: ", result)
```

- Explanation: Displays the sum of the entered numbers to the user.
- Why Display the Result: Informing the user of the outcome ensures clarity and completes the purpose of the program.

6. Continue or Exit Prompt:

```python
next_mov = input("Do you want to enter more numbers? (yes/no): ").strip().lower()
if next_mov != 'yes':
print("See you again!")
break
```

- Explanation: This section prompts the user to decide if they want to perform another calculation or exit. It uses .strip().lower() to standardize the input (e.g., "YES" becomes "yes"). If the user enters anything other than "yes", the program exits.
- Why Use strip() and lower(): These methods make the input case-insensitive and ignore accidental spaces, improving user experience by allowing flexible input formats.
- Why Use break: The break statement exits the loop, stopping the program when the user chooses not to continue.

7. if **name** == "**main**": main():

```python
if **name** == "**main**":
main()
```

- Explanation: This line ensures that main() is called only when the script is run directly. If the script is imported as a module, main() will not run automatically.
- Why Use if **name** == "**main**":: This conditional structure allows the program to be run as a standalone script and also to be imported into other scripts without executing immediately. It’s a Python best practice for scripts with a main function.

### Running the Program

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the program with:

```bash
python filename.py
```

4. Follow the on-screen prompts to enter numbers and calculate their sum. You can continue with new sets of numbers or exit the program at any time.

### Example Usage

```plaintext
Enter numbers separated by spaces: 5 10 15
The sum of the given numbers is: 30
Do you want to enter more numbers? (yes/no): yes
Enter numbers separated by spaces: 3 6 9
The sum of the given numbers is: 18
Do you want to enter more numbers? (yes/no): no
See you again!
```

> > Contributions are welcome! Thank you & happy coding!🙂
