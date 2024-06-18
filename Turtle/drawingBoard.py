import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("Drawing Board")

instance = turtle.Turtle()

def drawFunc():
    instance.forward(100)

def rotateAngelRight():
    instance.right(10)

def rotateAngelLeft():
    instance.left(10)

def clearScreen():
    instance.clear()

def returnHome():
    instance.home()

def dontWrite():
    instance.penup()

def write():
    instance.pendown()

drawingBoard.listen()
drawingBoard.onkey(fun=drawFunc, key="w")
drawingBoard.onkey(fun=rotateAngelRight, key="d")
drawingBoard.onkey(fun=rotateAngelLeft, key="a")
drawingBoard.onkey(fun=clearScreen, key="space")
drawingBoard.onkey(fun=returnHome(), key="enter")
drawingBoard.onkey(fun=dontWrite(), key="e")
drawingBoard.onkey(fun=write(), key="r")



turtle.mainloop()