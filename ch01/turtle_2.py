import random
import turtle
import turtle as t

swidth, sheight = 500, 500

t.shape("turtle")
t.title("랜덤으로 원그리기")
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.goto(0, -sheight / 2)
t.pendown()
t.speed(11)

for radius in range(1,250) :
    if radius % 6 == 0 :
        turtle.pencolor('red')
    elif radius % 5 == 0 :
        turtle.pencolor('yellow')
    if radius % 4 == 0 :
        turtle.pencolor('green')
    elif radius % 3 == 0 :
        turtle.pencolor('orange')
    if radius % 2 == 0 :
        turtle.pencolor('blue')
    elif radius % 1 == 0 :
        turtle.pencolor('purple')

        turtle.circle(radius)
t.done()