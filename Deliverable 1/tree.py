"""
Task by:
Oskar Nerheim
Lasse Lindholm
"""

from turtleplotlib import Turtle
import matplotlib.pyplot as plt

def generate_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current

def draw_lsystem(lsystem_string, step_length, angle):
    turtle = Turtle()
    stack = []
    
    for char in lsystem_string:
        if char == 'F':
            turtle.forward(step_length)
        elif char == 'X':
            pass  # No drawing operation
        elif char == '+':
            turtle.left(angle)
        elif char == '-':
            turtle.right(angle)
        elif char == '[':
            # Save current position and heading
            stack.append((turtle.x, turtle.y, turtle.direction))
        elif char == ']':
            # Restore previous position and heading
            turtle.up()  # Lift pen before moving
            x, y, direction = stack.pop()
            turtle.x = x
            turtle.y = y
            turtle.direction = direction
            turtle.down()  # Put pen down after restoring

# Define the L-system
axiom = "X"
rules = {
    'X': 'F-[[X]+X]+F[+FX]-X',
    'F': 'FF'
}

# Generate the fractal tree
iterations = 5
lsystem = generate_lsystem(axiom, rules, iterations)

# Draw the tree
step_length = 3
angle = 25
draw_lsystem(lsystem, step_length, angle)

# Show the result
plt.show()