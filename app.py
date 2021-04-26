# Logical operators ( and, or, not)
high_income = False
good_credit = True
student = False

# Using and both conditions need to be true
# using the or operator only one of the conditions needs to be true
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
