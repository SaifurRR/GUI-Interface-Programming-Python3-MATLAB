"""
This code uses the 'turtle' library to build a Robot with the Python Programming language. 
The turtle module draws a Robot by assembling each component separately.
"""

import turtle as t

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

# Function to draw the robot
def draw_robot():
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

    # Draw feet
    t.goto(-100, -150)
    draw_rectangle(50, 20, 'blue')
    t.goto(-30, -150)
    draw_rectangle(50, 20, 'blue')

    # Draw legs
    t.goto(-25, -50)
    draw_rectangle(15, 100, 'grey')
    t.goto(-55, -50)
    draw_rectangle(15, 100, 'grey')

    # Draw body
    t.goto(-90, 100)
    draw_rectangle(100, 150, 'red')

    # Draw arms
    t.goto(-150, 70)
    draw_rectangle(60, 15, 'grey')
    t.goto(-150, 110)
    draw_rectangle(15, 40, 'grey')
    t.goto(10, 70)
    draw_rectangle(60, 15, 'grey')
    t.goto(55, 110)
    draw_rectangle(15, 40, 'grey')

    # Draw neck
    t.goto(-50, 120)
    draw_rectangle(15, 20, 'grey')

    # Draw head
    t.goto(-85, 170)
    draw_rectangle(80, 50, 'red')

    # Draw eyes
    t.goto(-60, 160)
    draw_rectangle(30, 10, 'white')
    t.goto(-55, 155)
    draw_rectangle(5, 5, 'black')
    t.goto(-40, 155)
    draw_rectangle(5, 5, 'black')

if __name__ == "__main__":
    t.speed(0)  # Set the turtle drawing speed to the fastest
    draw_robot()
    t.done()
