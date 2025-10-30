"""
Deliverable 2 made by:
Oskar Nerheim
Lasse Lindholm
"""



from turtleplotlib import Turtle
import matplotlib.pyplot as plt
import math as math

class Rectangle:
    """
    Original Rectangle class fetched from jupyter notebook for week 8 in the INF201 canvas room.
    """
    def __init__(self, lower_left, upper_right, color = "blue", linewidth=2):
        assert isinstance(lower_left, tuple), "lower_left must be a tuple"
        assert isinstance(upper_right, tuple), "upper_right must be a tuple"
        assert len(lower_left) == 2, "lower_left must contain exactly 2 elements"
        assert len(upper_right) == 2, "upper_right must contain exactly 2 elements"
        
        self._linewidth = linewidth
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
        t.color(self._color)
        t.width(self._linewidth)

        #move to lower left corner and draw the rectangle
        t.up()
        t.x, t.y = self._lower_left
        t.setheading(0)
        t.down()
        for i in range(2):
            t.forward(self._width)
            t.left(90)
            t.forward(self._height)
            t.left(90)


class Triangle:
    def __init__(self, corner_1, corner_2, corner_3, color = "blue", linewidth=2):
        assert isinstance(corner_1, tuple), "corner 1 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 2 must be a tuple"
        assert isinstance(corner_1, tuple), "corner 3 must be a tuple"

        assert len(corner_1) == 2, "corner 1 tuple should contain 2 elements"
        assert len(corner_2) == 2, "corner 2 tuple should contain 2 elements"
        assert len(corner_3) == 2, "corner 3 tuple should contain 2 elements"
        
        self._linewidth = linewidth
        self._color = color

        self._corner1 = corner_1
        self._corner2 = corner_2
        self._corner3 = corner_3

        self._dx12 = self._corner2[0] - self._corner1[0]
        self._dy12 = self._corner2[1] - self._corner1[1]
        self._length1 = math.sqrt(self._dx12**2 + self._dy12 ** 2)

        self._dx23 = self._corner3[0] - self._corner2[0]
        self._dy23 = self._corner3[1] - self._corner2[1]
        self._length2 = math.sqrt(self._dx23**2 + self._dy23 ** 2)

        self._dx31 = self._corner1[0] - self._corner3[0]
        self._dy31 = self._corner1[1] - self._corner3[1]
        self._length3 = math.sqrt(self._dx31**2 + self._dy31 ** 2)
    
    def area(self):
                #Find the area of the triangle using Heron's formula
        semi_perimeter = (self._length1 + self._length2 + self._length3)/2 
        area = math.sqrt(semi_perimeter*(semi_perimeter - self._length1)*(semi_perimeter - self._length2)*(semi_perimeter - self._length3))
        return (f"area of the triangle is: {round(area, 3)}")
    
    def info(self):
        print(f"corner 1: {self._corner1}, corner 2: {self._corner2}, corner 3: {self._corner3}")
    
    def draw(self):
        #find the angles relative to the horizontal line
        

        angle12 = math.degrees(math.atan2(self._dy12, self._dx12))
        angle23 = math.degrees(math.atan2(self._dy23, self._dx23))
        angle31 = math.degrees(math.atan2(self._dy31, self._dx31))
        
        t.color(self._color)
        t.width(self._linewidth)

        t.up()
        t.x, t.y = self._corner1
        t.down()

        t.setheading(angle12)
        t.forward(self._length1)

        t.setheading(angle23)
        t.forward(self._length2)

        t.setheading(angle31)
        t.forward(self._length3)

class Circle:
    def __init__(self, center= (0,0), radius = 1, color = "blue", linewidth=2):

        assert isinstance(center, tuple), "center must be a tuple"
        assert len(center) == 2, "center must contain exactly 2 elements"
        assert radius > 0, "radius must be strictley positive"

        self._width = linewidth
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
        t.width(self._width)
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

    shapes = [  Rectangle((10, 10), (-40,40), linewidth=2, color="green"), 
                Rectangle((10,20), (20,30), linewidth=4), 
                Rectangle((20, 40), (30, 50), linewidth=2), 
                Circle(radius=10, color="orange")]
    
    shapes.append(Triangle((0, 0), (25, 25), (12, 0), color="red", linewidth=2))
    for shape in shapes:    
        shape.info()
        shape.area()
        shape.draw()
        print(shape.area())

    plt.show()
