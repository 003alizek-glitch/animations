import turtle as t
t.speed(0)
t.setpos(70, 0)
t.bgcolor("black")
for i in range(126):
    t.fd(i)
    t.rt(250)
    t.color("#059900")
    for a in range(3):
        t.fd(i)
        t.lt(40)
        t.circle(50, 30)
        t.hideturtle()
t.done()