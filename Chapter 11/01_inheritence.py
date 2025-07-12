class Employee:
    Company = "ITC"
    def show(self):
        print(f"THe name of the Employee is {self.name} and the saalary is {self.salary}")
# class Programmer:
#     Company = "ITC Infotech"
#     def show (self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer:
    Company = "ITC Infotec"
    def showLanguage(self):
        print(f"The name is  {self.name} and he is good with {self.showLanguage} language")

a = Employee()
b = Programmer()

print(a.Company)
print(b.Company)

  