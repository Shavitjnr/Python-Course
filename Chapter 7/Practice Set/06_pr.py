# 5! = 1X 2X 3X 4X 5X
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    product = 1
    product *= i
    print(f"The factorial of {n} is {product}") 