
class Complex:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"
    
    def __repr__(self):
        return f"Complex({self.a}, {self.b})"


z = Complex(1, 2)
y = Complex(3, 4)

print(z)
print([z, y])
print(Complex())
print(Complex(5))

