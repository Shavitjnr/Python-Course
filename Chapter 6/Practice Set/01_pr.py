a1 = int(input("Enter a number 1: "))
a2 = int(input("Enter a number 2: "))
a3 = int(input("Enter a number 3: "))
a4 = int(input("Enter a number 4: "))

if (a1 > a2 and a1 > a3 and a1 > a4):
    print("a1 is the largest number:", a1)
elif (a2 > a1 and a2 > a3 and a2 > a4):
    print("a2 is the largest number:", a2)  
elif (a3 > a1 and a3 > a2 and a3 > a4):
    print("a3 is the largest number:", a3)
elif (a4 > a1 and a4 > a2 and a4 > a3):
    print("a4 is the largest number:", a4)