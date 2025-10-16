from turtleplotlib import Turtle
import matplotlib.pyplot as plt



"""
Snowflake function gotten from the course notebook: INF201_H25_D1_Intro.ipynb
"""


def snowflake(turtle, depth):
    if depth == 0:
        turtle.forward(10)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1)  #                    F


"""
Our own complete snowflake function
Enter the amount of times it should complete the "snowflake" function to have more controll
"""

def complete_snowflake(turtle, depth, sides=3):
    """
    turtle : turtle object "Turtle(interactive=False)"
    depth : int, how deep the snowflake should go
    sides : int, how many times it should make turns and draw the snowflake function default = 3
    """
    turn = 360 / sides
    for i in range(sides):
        snowflake(turtle, depth)
        turtle.right(turn)

t = Turtle(interactive=False)

complete_snowflake(t, 2, sides=3)
plt.show()