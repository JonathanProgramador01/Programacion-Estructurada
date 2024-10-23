from turtle import  *



setup(1150,650,0,0)
title("Batman")
bgcolor("black")
shape("turtle")
width(5)




def fondo_batman():
    color("#FFD101")
    penup()
    goto(-10, 290)
    pendown()
    speed(0)
    begin_fill()
    for i in range(15):
        right(i)
        forward(50)
    for i in range(12, 2, -1):
        right(i)
        forward(50)

    forward(70)
    for i in range(15):
        right(i)
        forward(50)
    for i in range(12, 2, -1):
        right(i)
        forward(50)

    forward(30)
    end_fill()
def batman_derecho():
    color("black")
    penup()
    goto(5,-220)
    pendown()

    begin_fill()
    setheading(63)

    for i in range(0,15,2):
        right(i)
        forward(25)


    for i in range(15,18):
        right(i*2)
        forward(20)

    setheading(0)
    setheading(45)

    for i in range(0,15,2):
        right(i)
        forward(15)


    for i in range(15,19):
        right((i*2)-3)
        forward(22)

    for i in range(5):
        right(i)
        forward(17)

    setheading(0)

    for i in range(13,35,5):
        left(i)
        forward(100)

    left(30)
    forward(110)
    left(10)
    forward(110)
    left(10)
    forward(60)


    circle(80,-180)

    left(180)
    for i in range(2):
        forward(25)
        right(i)

    right(20)
    setheading(0)
    setheading(90)

    for i in range(3):
        left(i*2)
        forward(50)

    right(-140)

    for i in range(1,3):
        right(i*5)
        forward(55)

    setheading(0)
    setheading(-180)
    forward(45)
    end_fill()
def batman_izquierdo():
    color("black")
    penup()
    goto(7, -212)
    pendown()

    begin_fill()
    setheading(117)

    # Primer arco
    for i in range(0, 15, 2):
        left(i)
        forward(25)

    for i in range(15, 18):
        left(i * 2)
        forward(20)

    setheading(180)
    setheading(135)

    # Segundo arco
    for i in range(0, 15, 2):
        left(i)
        forward(15)


    for i in range(15, 19):
        left((i * 2) - 5)
        forward(22)

    for i in range(5):
        left(i)
        forward(17)

    setheading(180)

    # Controlar la curva con menos ángulo
    for i in range(13, 35, 5):
        right(i)
        forward(100)

    right(30)
    forward(110)
    right(10)
    forward(110)
    right(10)
    forward(60)


    circle(-80, -180)

    left(180)
    for i in range(2):
        forward(25)
        left(i)

    left(20)
    setheading(0)
    setheading(90)

    for i in range(3):
        right(i * 2)
        forward(50)

    left(-140)

    for i in range(1, 3):
        left(i * 5)
        forward(55)

    setheading(0)
    setheading(0)
    forward(45)
    hideturtle()
    end_fill()

fondo_batman()
batman_derecho()
batman_izquierdo()

penup()
goto(450, -320)
pendown()
color("#FFD101")
write('Autor: Jonathan', font=("Arial", 16, "normal"))


mainloop()