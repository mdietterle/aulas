import turtle

def inverteCor(cor):
    if(cor=='white'):
        tabuleiro.color('black')
        cor= 'black'
    else:
        tabuleiro.color('white')
        cor='white'
    print(cor)
    return cor

def main():
    tabuleiro.color('black')
    cor='black'
    desenhaXadrez(cor,0)
    tabuleiro.shape('circle')
    pecasJogador2()
    pecasJogador1()

def desenhaXadrez(cor,posy):
    for linhas in range(8):
        if(cor=='white'):
            cor='black'
        else:
            cor='white'
        for contador in range(8):
            tabuleiro.begin_fill()
            tabuleiro.color('black',cor)
            tabuleiro.forward(40)
            tabuleiro.left(90)
            tabuleiro.forward(40)
            tabuleiro.left(90)
            tabuleiro.forward(40)
            tabuleiro.left(90)
            tabuleiro.forward(40)
            tabuleiro.left(90)
            tabuleiro.forward(40)
            tabuleiro.end_fill()
            if(cor=='white'):
                cor='black'
            else:
                cor='white'
        tabuleiro.setx(0)
        posy=posy+40
        tabuleiro.sety(posy)

def pecasJogador1():
    tabuleiro.penup()
    tabuleiro.speed(10)
    posy=-20
    #tabuleiro.sety(20)
    for pecaslinhas in range(2):
        posy=posy+40
        tabuleiro.setx(20)
        tabuleiro.sety(posy)
        for pecas in range(8):
            tabuleiro.pendown()
            tabuleiro.begin_fill()
            tabuleiro.color('blue','blue')
            tabuleiro.stamp()
            stamp_blue.append(turtle.stamp())
            tabuleiro.end_fill()
            tabuleiro.penup()
            if(pecas < 7):
                tabuleiro.forward(40)
    print('blue=',stamp_blue)
    turtle.exitonclick()

def pecasJogador2():
    tabuleiro.penup()
    tabuleiro.speed(10)
    posy=360-20
    #tabuleiro.sety(20)
    for pecaslinhas in range(2):
        posy=posy-40
        tabuleiro.setx(20)
        tabuleiro.sety(posy)
        for pecas in range(8):
            tabuleiro.pendown()
            tabuleiro.begin_fill()
            tabuleiro.color('red','red')
            tabuleiro.stamp()
            stamp_red.append(turtle.stamp())
            tabuleiro.end_fill()
            tabuleiro.penup()
            tabuleiro.forward(40)
    print('red=',stamp_red)
    #turtle.exitonclick()
    
cor='white'
tabuleiro=turtle.Turtle()
tabuleiro.speed(1000)
posy=-40
stamp_blue=[]
stamp_red=[]
main()
