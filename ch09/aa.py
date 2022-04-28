import random
import tkinter
# import tkinter as tk
# from tkinter.simpledialog import *
import turtle as t
swidth, sheight = 500, 500
txtSize = 30
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
retStr = tkinter.simpledialog.askstring('Input char', 'Input for turtle')
for i in range(len(retStr)):
    x= random.randrange(-200,200)
    y= random.randrange(-200,200)
    r = random.random()
    g = random.random()
    b = random.random()
    t.up()
    t.goto(x,y)
    t.down()
    t.color((r,g,b))
    t.write(retStr[i], font=('맑은고딕', txtSize, 'bold'))

t.done()