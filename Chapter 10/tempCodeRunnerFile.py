class Employee:
    language = "Python"  # class attribute
    salary = 1200000      # class attribute

    def __init__(self, name,salary, language):     # dunder method for initialization
        self.name = name
        self.salary = salary
        self.language = language
        print("I am Creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    def greet(self):
        print("Good Morning!! Baby Gurls!!")

shavit = Employee("Shavit", 1300000, "JavaScript")  # creating an object
shavit.name = "Shavit"  # instance attribute
print(shavit.name, shavit.salary)  # accessing instance attribute   

rohan = Employee()