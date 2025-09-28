from turtle import *
speed(0)
setpos(-200, -150)
color("red")
bgcolor('black')
pensize(2)
def tri(x):
    for i in range(3):
        fd(x)
        lt(120)
        x -= 10
x = 400
for j in range(13):
    tri(x)
    x -= 30
    hideturtle()
done()