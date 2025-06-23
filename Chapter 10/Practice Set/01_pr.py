class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary,PIN):
        self.name = name
        self.salary = salary
        self.PIN = PIN

p = Programmer("Shavit", 1200000, 1234)
print(p.name, p.salary, p.PIN)  # accessing instance attributes

r = Programmer(name="Rohan", salary=1500000, PIN=5678)  # creating another object
print(r.name, r.salary, r.PIN)  # accessing instance attributes