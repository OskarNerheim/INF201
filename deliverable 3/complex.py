
class Complex:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"
    
    def __repr__(self):
        return f"Complex({self.a}, {self.b})"

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return f"{new_a} + {new_b}i"
        

z = Complex(1, 2)
y = Complex(3, 4)

print(z)
print([z, y])
print(Complex())
print(Complex(5))

print(z + y)

