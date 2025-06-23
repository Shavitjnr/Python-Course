class Employee:
    name = "Shavit"
    language = "Python"     # class attributes
    salary = 1200000

harry = Employee()
harry.name = "Harry"        # object/instance attribute
print(harry.name,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,rohan.salary, rohan.language)

# rohan = Employee()
# print(rohan.language, rohan.salary)
# rohan.language = "Java"
# print(rohan.language, rohan.salary)


# Here name is object attribute and salary and language are class attributes as they directly belong to the class. 