
class Complex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def __str__(self):
        return f"{self.a} + {self.b}i"
    
    def __repr__(self):
        return f"Complex({self.a}, {self.b})"

    def __add__(self, other):
        new_re = self.re + other.re
        new_im = self.im + other.im
        return f"{new_re} + {new_im}i"

    def __sub__(self, other):
        new_re = self.re - other.im
        new_im = self.re - other.im
        return f"{new_re} + {new_im}i"
        

z = Complex(1, 2)
y = Complex(3, 4)

print(z)
print([z, y])
print(Complex())
print(Complex(5))

print(z + y)

