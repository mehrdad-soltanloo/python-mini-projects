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
        
    
    
                         


