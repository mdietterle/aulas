import turtle

star=turtle.Pen()
star.color('blue')
star.begin_fill()

for i in range(5):
    star.forward(50)
    star.right(144)
star.end_fill()
print("Clique para sair")
turtle.exitonclick()