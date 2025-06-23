class Calculater:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(self.n * self.n)
    def cube(self):
        print(self.n * self.n * self.n)
    def squareRoot(self):
        print(self.n ** 0.5)

a = Calculater(5)
a.square()  # calling the square method to print the square of n
a.cube()    # calling the cube method to print the cube of n
a.squareRoot()  # calling the squareRoot method to print the square root of n