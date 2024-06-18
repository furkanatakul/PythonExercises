import turtle
import time
from random import randint

count = 0
def countClick(x, y):
    global count
    count += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {count}", align="center", font=("Arial", 24, "normal"))
    object_turtle.onclick(None)

screenTime = 30

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Python Turtle Graphics")
screen.setup(width=800, height=800)

# Create the turtle for displaying score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, screen.window_height() // 2 * 0.85)
score_turtle.color("blue")
score_turtle.write(f"Score: {count}", align="center", font=("Arial", 24, "normal"))

# Create the turtle for displaying time
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.goto(0, screen.window_height() // 2 * 0.70)

# Create the turtle for the moving object
object_turtle = turtle.Turtle(shape='turtle')
object_turtle.shapesize(stretch_wid=2, stretch_len=2, outline=1)
object_turtle.penup()
object_turtle.color("green")
object_turtle.speed('fastest')

# Main game loop
while screenTime > 0:
    time_turtle.clear()
    time_turtle.write(f"Time: {screenTime}", align="center", font=("Arial", 24, "normal"))

    for _ in range(2):
        max_x = screen.window_width() // 2 - 20
        max_y = screen.window_height() // 2 - 20
        object_turtle.setposition(randint(-max_x, max_x), randint(-max_y, max_y))
        object_turtle.onclick(countClick)
        time.sleep(0.6)

    screenTime -= 1

time_turtle.clear()
object_turtle.hideturtle()
time_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))

turtle.mainloop()