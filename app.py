# Chain Comparison operators

# age should be between 18 and 65

age = 22
if age >= 18 and age < 65:
    print("Eligible")
# This line does the same as teh line above.
# This line is cleaner and this is how we chain comparison operators.
if 18 <= age < 65:
