### Lab1: A function that takes an input from the user and calculate someone’s age

from datetime import date

def calculate_age():
    try:
        current_date = date.today()

        birth_date = input("Enter your birthdate (YYYY-MM-DD): ")

        birth_date = date.fromisoformat(birth_date)

        age = current_date.year - birth_date.year

        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    except TypeError:
        print("Please enter a valid integer for the birthdate.")

age = calculate_age()
print("Your age is:", age)


def helloWorld():
	print(‘Hello World’)

helloWorld()

