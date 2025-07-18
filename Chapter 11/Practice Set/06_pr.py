class Vactor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z    

    def __add__(self, other):
        result = Vactor(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y, self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
# Test the implementation
v1 = Vactor(1, 2, 3)
v2 = Vactor(4, 5, 6)
v3 = Vactor(7, 8, 9)    #   Same dimentions vector

print(v1 + v2)  # Output: Vector(5, 6, 7)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50