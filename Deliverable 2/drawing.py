from turtleplotlib import Turtle
import matplotlib.pyplot as plt
import math

class Rectangle:
    """
    Original Rectangle class fetched from jupyter notebook for week 8 in the INF201 canvas room.
    """
    def __init__(self, lower_left, upper_right):
        assert isinstance(lower_left, tuple), "lower_left must be a tuple"
        assert isinstance(upper_right, tuple), "upper_right must be a tuple"
        assert len(lower_left) == 2, "lower_left must contain exactly 2 elements"
        assert len(upper_right) == 2, "upper_right must contain exactly 2 elements"
        
        self._lower_left = lower_left
        self._upper_right = upper_right
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]

    def info(self):
        print(f"Upper right: {self._upper_right}, Lower Left: {self._lower_left}")
        
    def area(self):
        return self._width * self._height

    def draw(self):
        #move to lower left corner and draw the rectangle
        t.up()
        t.x, t.y = self._lower_left
        t.down()
        for i in range(2):
            t.forward(self._width)
            t.left(90)
            t.forward(self._height)
            t.left(90)


class Triangle:
    def __init__(self, corner_1, corner_2, corner_3):
        assert isinstance(corner_1, tuple), "corner 1 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 2 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 3 must be a tuple"

        assert len(corner_1) == 2, "corner 1 tuple should contain 2 elements"
        assert len(corner_2) == 2, "corner 2 tuple should contain 2 elements"
        assert len(corner_3) == 2, "corner 3 tuple should contain 2 elements"

        self._corner1 = corner_1
        self._corner2 = corner_2
        self._corner3 = corner_3

if __name__ == "__main__":
    
    t = Turtle(interactive=False)

    shapes = [Rectangle((10, 10), (20,20)), Rectangle((10,20), (20,30)), Rectangle((20, 40), (30, 50))]
    for shape in shapes:    
        shape.info()
        shape.draw()
    
    plt.show()
