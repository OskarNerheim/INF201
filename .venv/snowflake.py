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


t = Turtle(interactive=False)

snowflake(t, 4)
plt.show()