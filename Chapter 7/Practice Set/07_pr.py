'''
  *
 ***
*****
'''

n = int(input("Enter the number of rows: "))
# print(" " * (n - 1))
# print("*"* (n-1))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")