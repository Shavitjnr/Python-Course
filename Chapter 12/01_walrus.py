# Advance Python Course - Chapter 12

# Using Walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3).")
