import turtle as t
t.speed(0)
t.bgcolor("black")
t.pensize(2)
for i in range(126):
    t.fd(i)
    t.rt(150)
    t.color("#909090")
    for a in range(2):
        t.fd(i)
        t.lt(35)
        t.hideturtle()
t.done()