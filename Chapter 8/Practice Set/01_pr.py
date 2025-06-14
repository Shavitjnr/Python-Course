#   Write a program using function to find greatest of three number 
def greatest(a,b,c):
    if(a>b and a> c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = int(input("Enter the first Number: "))
b = int(input("Enter the second Number: "))
c = int(input("Enter the third Number: "))
print(greatest(a,b,c))