import os


def get_user_list():
    choice = input("Enter '1' to input a list or '2' to use a default list: ")
    if choice == "1":
        user_input = input("Enter numbers separated by spaces: ")
        return list(map(int, user_input.split()))
    else:
        return [10, 25, 45, 75, 95]
    

def display_menu():
    print("\nWhat would you like to do?")
    print("1. Reverse the list.")    
    print("2. Sort the list.")    
    print("3. Remove duplicates.")    
    print("4. Filter even numbers.")    
    print("5. Filter odd numbers.")    
    print("6. Save a list to a file.")    
    print("7. Exit.")    

def reverse_list(numbers):
    numbers.reverse()
    print(f"Reversed list: {numbers}")

def sort_list(numbers):
    choice =  input("Enter '1' for ascending or '2' for descending sort: ")
    if choice == '1':
        sorted_list = sorted(numbers)
    else:
        sorted_list = sorted(numbers, reverse=True)
    print(f"Sorted list: {sorted_list}")     
    return sorted_list

def remove_duplicates(numbers):
    unique_numbers = list(dict.fromkeys(numbers))
    print(f"List without duplicates: {unique_numbers}")
    return unique_numbers

def filter_list(numbers, even=True):
    numbers_copy = numbers[:]
    if even:
        filtered = [num for num in numbers_copy if num % 2 == 0]
        print(f"Even numbers: {filtered}")
    else:
        filtered = [num for num in numbers_copy if num % 2 != 0 ]
        print(f"Odd numbers: {filtered}")
    return filtered        

def save_to_file(numbers):

    if not os.path.exists("saved_file"):
        os.makedirs("saved_file")

    filename = input("Enter the filename to save the list: ")

    filepath = os.path.join("saved_file", filename)

    with open(filepath, "w") as file:
        file.write(', '.join(map(str, numbers)))
        print(f"List saved to {filename}")      

def main():
    numbers = get_user_list()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            reverse_list(numbers)
        elif choice == "2":
            numbers = sort_list(numbers)
        elif choice == "3":
            numbers = remove_duplicates(numbers)
        elif choice == "4":
            filter_list(numbers, even=True)
        elif choice == "5":
            filter_list(numbers, even=False)
        elif choice == "6":
            save_to_file(numbers) 
        elif choice == "7":
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
            




