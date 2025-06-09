a = int(input("Enter a number: "))
if (a >= 18):
    print("You are eligible for voting")
    print("You have right to do this")
elif (a < 0):
    print("You are entering an invalid age")
    print("Please enter a valid age")
elif (a == 0):
    print("You are not eligible for voting")
    print("You are too young to vote")
else:
    print("You are not eligible for voting")
    print("You do not have right to do this")

print("End of program")