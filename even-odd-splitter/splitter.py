#!/usr/bin/env python3

def get_numbers():
    # Prompt user for input and validate that input is all integers
    while True:
        user_input = input("Enter a list of numbers separated by spaces: ")
        try:
            # Convert input to a list of integers
            return [int(num) for num in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")

def split_even_odd(numbers):
    # Separate numbers into even and odd lists
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

def display_results(even_numbers, odd_numbers):
    # Display even and odd numbers lists
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

def main():
    numbers = get_numbers()                 # Step 1: Get and validate user input
    even_numbers, odd_numbers = split_even_odd(numbers)  # Step 2: Split numbers into even and odd
    display_results(even_numbers, odd_numbers)           # Step 3: Display the results

if __name__ == "__main__":
    main()


 
       

    