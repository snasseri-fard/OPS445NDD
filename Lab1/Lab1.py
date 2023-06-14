### Lab1: A function that takes an input from the user and calculate someone’s age

from datetime import date

def calculate_age():
    # Get the current date
    current_date = date.today()

    # Prompt the user for their birthdate
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")

    # Convert the input into a date object
    birth_date = date.fromisoformat(birth_date)

    # Calculate the age
    age = current_date.year - birth_date.year

    # Check if the birthday hasn't happened yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# Example usage:
age = calculate_age()
print("Your age is:", age)

