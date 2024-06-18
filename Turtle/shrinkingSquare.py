import turtle

screen = turtle.Screen()
screen.bgcolor("light green")
screen.title("squares")

nesne = turtle.Turtle()
nesne.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        nesne.forward(size)
        nesne.left(90)
        size -= 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)




turtle.done()