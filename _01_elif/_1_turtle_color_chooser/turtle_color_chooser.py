import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    bob = turtle.Turtle()
    bob.width(10)
    color = simpledialog.askstring(title="Color Chooser", prompt="Choose what color the circle should be!")
    if color == "red":
        bob.pencolor('red')
    elif color == "orange":
        bob.pencolor('orange')
    elif color == "yellow":
        bob.pencolor('yellow')
    elif color == "green":
        bob.pencolor("green")
    elif color == "blue":
        bob.pencolor('blue')
    elif color == "purple":
        bob.pencolor('purple')
    else: bob.pencolor(get_random_color())
    bob.circle(100)
    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
