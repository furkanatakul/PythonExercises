import turtle
import random
screen = turtle.Screen()
screen.bgcolor("red")
screen.title("Helix")

instance = turtle.Turtle()
instance.color("white")
colorsList = ["blue", "yellow", "purple", "orange"]

for i in range(9):
    instance.circle(30*i)
    instance.circle(-30 *i)
    instance.right(10 * i)
    instance.color(colorsList[random.randint(0,3)])

turtle.done()