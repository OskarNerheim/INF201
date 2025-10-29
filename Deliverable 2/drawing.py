
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



if __name__ == "__main__":
    shapes = [Rectangle((1,1), (2,2)), Rectangle((0,0), (2,3))]
    for shape in shapes:
        print(shape.area())
        shape.info()
