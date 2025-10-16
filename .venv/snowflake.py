from turtleplotlib import Turtle
import matplotlib.pyplot as plt



"""
Snowflake function gotten from the course jupyter notebook: INF201_H25_D1_Intro.ipynb

Edited snowflake function to include size.

"""


def snowflake(turtle, depth, size):
    if depth == 0:
        turtle.forward(size)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1, size)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1, size)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1, size)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1, size)  #                    F


"""
Our own complete snowflake function
"""

def complete_snowflake(turtle, depth, sides=3, size = 10, linewidth=1, color="red"):
    """
    turtle : turtle object "Turtle(interactive=False)"
    depth : int, how deep the snowflake should go
    sides : int, how many times it should make turns and draw the snowflake function default = 3
    size : int, distance the turtle should travel before turning
    linewidth : int, the width of the line
    coolor: string, the color of the line
    """

    turtle.color(color)
    turtle.width(linewidth)
    turn = 360 / sides
    for i in range(sides):
        snowflake(turtle, depth, size)
        turtle.right(turn)

t = Turtle(interactive=False)

complete_snowflake(t, 2, sides=3, size=10, linewidth=4, color="red")
plt.show()