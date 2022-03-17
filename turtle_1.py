import turtle
import random


# 함수 선언 부분 ##

def screenLeftclick(x, y):
    global r, g, b
    global pSize

    r = random.random()
    g = random.random()
    b = random.random()
    pSize = random.random(1, 10)

    turtle.shapesize(pSize)
    turtle.pencolor((r, g, b)
    turtle.pendown()
    turtle.goto(x.y)

    ##변수 선언 부분 ##
    pSize = 10
    r == 0.0
    g = 0.0
    b = 0.0

    ## 메인 코드 부분 ##
    turtle.turtles('거북이로 그림 그리기')
    turtle.shape('turtle')
    turtle.pensize()



