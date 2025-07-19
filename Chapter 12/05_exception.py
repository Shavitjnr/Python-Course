try:
    a = int(input("Hey, Enter a number: "))
    print("You entered:", a)

except ValueError as v:
    print("Hello...")
    print(v)
except Exception as e:
    print(e)
    
print("Thank You!! ")
