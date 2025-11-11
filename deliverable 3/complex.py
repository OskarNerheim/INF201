
class Complex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def __str__(self):
        return f"{self.re}+{self.im}i"
    
    def __repr__(self):
        return f"Complex({self.re}, {self.im})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
    
    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        new_re = self.re - other.re
        new_im = self.im - other.im
        return f"{new_re}+{new_im}i"

    def __mul__(self, other):
        new_re = (self.re * other.re) - (self.im * other.im)
        new_im = (self.re * other.im) + (self.im * other.re)
        return f"{new_re}+{new_im}i"

    def __eq__(self, other):
        return ((self.re == other.re) and (self.im == other.im))

    def __ne__(self, other):
        return (self.re != other.re) or (self.im != other.im)

z = Complex(1, 2)
y = Complex(3, 4)

print(z)
print([z, y])
print(Complex())
print(Complex(5))

print(z + y)
print(y - z)
