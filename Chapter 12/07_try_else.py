try:
    
    a = int(input("Enter a number: "))
    print(a)
# except ValueError as v:
#     print("Hii...")
#     print(v)

except Exception as e:
    print("Wrong Number ", e)

else:
    # print("Thank You!!")
    print("I am inside else block")