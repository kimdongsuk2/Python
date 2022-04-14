import turtle as t
t.shape("turtle")
t.color("red")
t.bgcolor("yellow")
t.fillcolor("blue")
t.begin_fill()
t.circle(100)
t.end




for i in range(0,100):
    t.forward(100+ i)
    t.right(30+ i)


t.done()