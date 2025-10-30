import math as math

class Rectangle:
    def __init__(self, lower_left, upper_right):
        assert isinstance(lower_left, tuple), "lower_left must be a tuple"
        assert isinstance(upper_right, tuple), "upper_right must be a tuple"
        assert len(lower_left) == 2, "lower_left must contain exactly 2 elements"
        assert len(upper_right) == 2, "upper_right must contain exactly 2 elements"
        
        self._ll = lower_left
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]
        self._lower_left = lower_left
        self._upper_right = upper_right

    def info(self):
        print(f"Upper right: {self._upper_right}, Lower Left: {self._lower_left}")
        
    def area(self):
        return self._width * self._height

class Circle:
    def __init__(self, center= (0,0), radius = 1):
        assert isinstance(center, tuple), "center must be a tuple"
        assert len(center) == 2, "center must contain exactly 2 elements"
        assert radius > 0, "radius must be strictley positive"
        self._center = center
        self._x = center[0]
        self._y = center[1]
        self._radius = radius
        self._diameter = self._radiusa*2
    
    def info(self):
        print(f"Center: {self._center}, radius: {self._radius}")

    def area(self):
        return math.pi * self._radius**2
    
    def draw(self):
        



if __name__ == "__main__":
    shapes = [Rectangle((1,1), (2,2)), Rectangle((0,0), (2,3))]
    for shape in shapes:
        print(shape.area())
        shape.info()
