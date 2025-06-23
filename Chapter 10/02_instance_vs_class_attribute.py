class Employee:
    language = "Python"  # class attribute
    salary = 1200000      # class attribute

harry = Employee()
harry.language = "JavaScript"  # instance attribute
print(harry.language, harry.salary)