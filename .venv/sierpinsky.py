from turtleplotlib import Turtle
import matplotlib.pyplot as plt


def sierpinski(turtle, depth):
    sierpinskiA(turtle, depth)

#Draws the curve as blue when drawing A
def sierpinskiA(turtle, depth):
    turtle.color("blue")
    if depth == 0:
        turtle.forward(10)
    else:
        sierpinskiB(turtle, depth-1)
        turtle.left(60)
        sierpinskiA(turtle, depth-1)
        turtle.left(60)
        sierpinskiB(turtle, depth-1)

#Draws the curve as red when drawing B
def sierpinskiB(turtle, depth):
    turtle.color("red")
    if depth == 0:
        turtle.forward(10)
    else:
        sierpinskiA(turtle, depth-1)
        turtle.right(60)
        sierpinskiB(turtle, depth-1)
        turtle.right(60)
        sierpinskiA(turtle, depth-1)


t = Turtle(interactive=False)
sierpinski(t, 5)

plt.show()