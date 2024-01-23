# Write a program to check if the given number is a palindrome number.

# Pseudocode

# Ask user to input  numbers
user_input = input("Please enter numbers: ")

# Create funtion to check if the input numbers are palindrome
def is_palindrome(user_input):
    # In the function, create a if-else statement
    if user_input == user_input[::-1]:
    # If input number is palindrome return True
        return True
    # Else, False
    else: 
        return False
    
# Print the result
result = is_palindrome(user_input)
if result:
    print(f"Number {user_input} is a palindrome.")
else:
    print(f"Number {user_input} is not a palindrome.")


