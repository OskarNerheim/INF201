"""
Oblig partners:
Lasse Lindholm
Oskar Nerheim
"""


class Complex:
    """
    Simple function for complex numbers that support different operations
    """
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b


    def __str__(self):
        sign = "+" if self.im >= 0 else "-"
        imag_abs = abs(self.im)
        return f"{self.re}{sign}{imag_abs}i"


    def __repr__(self):
        return f"Complex({self.re}, {self.im})"


    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        
        if isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        return NotImplemented


    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other + self.re, self.im)
        
        if isinstance(other, Complex):
            return Complex(other.re + self.re, other.im + self.im)
        return NotImplemented


    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        
        if isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        return NotImplemented


    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.re, -self.im)
        
        if isinstance(other, Complex):
            return Complex(other.re - self.re, other.im - self.im)
        return NotImplemented


    def __mul__(self, other):
        if isinstance(other, Complex):
            new_re = (self.re * other.re) - (self.im * other.im)
            new_im = (self.re * other.im) + (self.im * other.re)
            return Complex(new_re, new_im)
        
        if isinstance(other, (int, float)):
            return Complex(self.re * other, self.im * other)
        return NotImplemented


    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return (self * other)

        if isinstance(other, Complex):
            new_re = (other.re * self.re) - (other.im * self.im)
            new_im = (other.re * self.im) + (other.im * self.re)
            return Complex(new_re, new_im)
        return NotImplemented


    def __eq__(self, other):
        if not isinstance(other, Complex):
            return False
        return (self.re == other.re) and (self.im == other.im)


    def __ne__(self, other):
        return not self.__eq__(other)