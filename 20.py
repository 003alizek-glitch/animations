from turtle import *
from colorsys import *
speed(0)
width(2)
bgcolor('black')
h = 0
for i in range(70):
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    begin_fill()
    circle(i, 216)
    circle(i, -144)
    rt(100)
    h += 0.006
    end_fill()
hideturtle()
done()