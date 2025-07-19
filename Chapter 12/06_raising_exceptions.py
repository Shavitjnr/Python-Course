a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("Division by zero error")
else:
    print("The result of division is:", a / b)