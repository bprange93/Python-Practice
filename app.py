# Short cut to run code Ctrl Alt n.
first = "Brandon"
last = "Prange"
# This is the same as setting variable to print = to first + " " + last.
# Cleaner way to doing it and not having to worry about the space with quotes.
# This is a formatted string. It can be used many different ways and can call methods inside of it.

full = f"{first} {last}"
full2 = f"{len(first)} {last}"
full3 = f"{len(first)} {2 + 2}"
print(full)
print(full2)
print(full3)
