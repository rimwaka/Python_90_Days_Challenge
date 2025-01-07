# Day 2: Variables and Data Types
# Importing the datetime library
import datetime

# Prompting the user for their name
name = input("Please enter your name: ")

# Function to get a valid age between 0 and 99
def get_valid_age():
    while True:
        try:
            # Prompt the user for their age
            age = int(input("Enter your age (0-99): "))
            # Check if the age is within the valid range
            if 0 <= age <= 99:
                return age
            else:
                print("Age must be between 0 and 99. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get the user's age
age = get_valid_age()

# Using the datetime library to get the current date
current_date = datetime.datetime.now()

# Getting the current year
current_year = current_date.year

# Calculating the year of birth for the person
year_of_birth = current_year - age

# Printing a greetings message
print(f"Hello {name}, you have a beautiful name.")
print(f"You're of good age, {age}, and you were born in {year_of_birth}.")

#Output
#Please enter your name: Mwehu
#Enter your age (0-99): 21
#Hello Mwehu, you have a beautiful name.
#You're of good age, 21, and you were born in 2004.
