from turtleplotlib import Turtle
import matplotlib.pyplot as plt


class Rectangle:
    """
    Original Rectangle class fetched from jupyter notebook for week 8 in the INF201 canvas room.
    """
    def __init__(self, lower_left, upper_right):
        assert isinstance(lower_left, tuple), "lower_left must be a tuple"
        assert isinstance(upper_right, tuple), "upper_right must be a tuple"
        assert len(lower_left) == 2, "lower_left must contain exactly 2 elements"
        assert len(upper_right) == 2, "upper_right must contain exactly 2 elements"
        
        self.lower_left = lower_left
        self.upper_right = upper_right
        self.width = upper_right[0] - lower_left[0]
        self.height = upper_right[1] - lower_left[1]

    def info(self):
        print(f"Upper right: {self.upper_right}, Lower Left: {self.lower_left}")
        
    def area(self):
        return self.width * self.height

    def draw(self):
        #move to lower left corner and draw the rectangle
        t.up()
        t.x, t.y = self.lower_left
        t.down()
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)



if __name__ == "__main__":
    
    t = Turtle(interactive=False)

    shapes = [Rectangle((10, 10), (20,20)), Rectangle((10,20), (20,30)), Rectangle((20, 40), (30, 50))]
    for shape in shapes:    
        shape.info()
        shape.draw()
    
    plt.show()
