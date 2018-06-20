import turtle

turtle.bgcolor("#c2c2c2")

def drawRect(color):
    itterations = 0
    turtle.begin_fill() # Begin the fill process.
    turtle.down()
    turtle.color(color)

    while itterations < 4:
        turtle.forward(40)
        turtle.left(90)
        itterations += 1

    turtle.up() # Pen up
    turtle.end_fill()


def pushTurtleForward():
    turtle.forward(40)


def drawHorizontal(inverted):
    if(inverted):
        for horizontal in range(0, 8):
            if(horizontal > 0 and horizontal % 2 != 0):
                pushTurtleForward()
                drawRect("white")
            if(horizontal > 0 and horizontal % 2 == 0):
                pushTurtleForward()
                drawRect("black")
            if(horizontal == 0):
                drawRect("black")
    else:
        for horizontal in range(0, 8):
            if(horizontal > 0 and horizontal % 2 != 0):
                pushTurtleForward()
                drawRect("black")
            if(horizontal > 0 and horizontal % 2 == 0):
                pushTurtleForward()
                drawRect("white")
            if(horizontal == 0):
                drawRect("white")

for drawVertical in range(0, 8):
    turtle.setx(0)
    turtle.sety(40 * drawVertical)
    if(drawVertical % 2 == 0):
        drawHorizontal(inverted=True)
    else:
        drawHorizontal(inverted=False)

turtle.setx(0)
turtle.sety(0)
turtle.done()