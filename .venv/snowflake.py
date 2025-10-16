from turtleplotlib import Turtle
import matplotlib.pyplot as plt

t = Turtle(interactive=False)

t.forward(100)
t.left(90)
t.color("red")
t.forward(50)

print("done")

plt.show()  # <-- this displays the drawing window
