from turtleplotlib import Turtle
import matplotlib.pyplot as plt
import math as math

class Rectangle:
    """
    Original Rectangle class fetched from jupyter notebook for week 8 in the INF201 canvas room.
    """
    def __init__(self, lower_left, upper_right, color = "blue"):
        assert isinstance(lower_left, tuple), "lower_left must be a tuple"
        assert isinstance(upper_right, tuple), "upper_right must be a tuple"
        assert len(lower_left) == 2, "lower_left must contain exactly 2 elements"
        assert len(upper_right) == 2, "upper_right must contain exactly 2 elements"
        
        self._color = color
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
        t.color(self._color)
        t.up()
        t.x, t.y = self._lower_left
        t.down()
        for i in range(2):
            t.forward(self._width)
            t.left(90)
            t.forward(self._height)
            t.left(90)


class Triangle:
    def __init__(self, corner_1, corner_2, corner_3, color = "blue"):
        assert isinstance(corner_1, tuple), "corner 1 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 2 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 3 must be a tuple"

        assert len(corner_1) == 2, "corner 1 tuple should contain 2 elements"
        assert len(corner_2) == 2, "corner 2 tuple should contain 2 elements"
        assert len(corner_3) == 2, "corner 3 tuple should contain 2 elements"
        
        self._color = color
        self._corner1 = corner_1
        self._corner2 = corner_2
        self._corner3 = corner_3
    
    def area(self):
        length1_x = math.abs(self._corner1[0] - self._corner1[0])
        length1_y = math.abs(self._corner1[1] - self._corner1[1])
        length1 = math.sqrt(length1_x**2 + length1_y ** 2)

        length2_x = math.abs(self._corner2[0] - self._corner2[0])
        length2_y = math.abs(self._corner2[1] - self._corner2[1])
        length2 = math.sqrt(length2_x**2 + length2_y ** 2)

        length3_x = math.abs(self._corner3[0] - self._corner3[0])
        length3_y = math.abs(self._corner3[1] - self._corner3[1])
        length3 = math.sqrt(length3_x**2 + length3_y ** 2)

        #Find the area of the triangle using Heron's formula
        semi_perimeter = (length1 + length2 + length3)/2 
        area = math.sqrt(semi_perimeter*(semi_perimeter - length1)*(semi_perimeter - length2)*(semi_perimeter - length3))
        print(area)
    
    def info(self):
        print(f"corner 1: {self._corner1}, corner 2: {self._corner2}, corner 3: {self._corner3}")

class Circle:
    def __init__(self, center= (0,0), radius = 1, color = "blue"):

        assert isinstance(center, tuple), "center must be a tuple"
        assert len(center) == 2, "center must contain exactly 2 elements"
        assert radius > 0, "radius must be strictley positive"

        self._color = color
        self._center = center
        self._x = center[0]
        self._y = center[1]
        self._radius = radius
        self._diameter = self._radius*2
        self._sides = 360
        self._angle_in_poligon = (self._sides - 2)/self._sides
        self._side_length = 2 * self._radius * math.sin(math.pi/self._sides)
    
    def info(self):
        print(f"Center: {self._center}, radius: {self._radius}")

    def area(self):
        return math.pi * self._radius**2
    
    def draw(self):
        t.color(self._color)
        t.up()
        t.goto(self._center)
        t.setheading(0)
        t.forward(self._radius)
        t.down()
        t.right(90)
        for i in range(self._sides):
            t.right(self._angle_in_poligon)
            t.forward(self._side_length)
            


if __name__ == "__main__":
    
    t = Turtle(interactive=False)

    shapes = [Rectangle((-10, -10), (10,10)), Rectangle((10,20), (20,30)), Rectangle((20, 40), (30, 50)), Circle(radius=10)]
    for shape in shapes:    
        shape.info()
        shape.draw()
        print(shape.area())
    
    plt.show()
