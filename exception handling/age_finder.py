try:
    birth_year = int(input("Which year were you born? "))
    current_year = 2024
    age = current_year - birth_year
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid numeric value.")
finally:
    print("Back to the program.")