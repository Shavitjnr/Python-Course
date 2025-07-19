from functools import reduce
# Map Function Example
l = [1, 2, 3, 4, 5]

square = lambda n: n * n
sqList = map(square, l)
print(list(sqList))
# Filter Function Example

def even(n):
    if n % 2 == 0:
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Function Example
def sum(a, b):
    return a + b
mul = lambda a, b: a * b
print(reduce(sum, l))
print(reduce(mul, l))