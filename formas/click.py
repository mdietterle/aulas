import turtle
def getPos(x,y):
    turtle.color('red','red')
    print("(", int(x), "," ,int(y),")")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(51)
    turtle.end_fill()
    return

def main():
    turtle.onscreenclick(getPos)
    turtle.mainloop()
main()