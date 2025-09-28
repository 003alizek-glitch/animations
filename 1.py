import turtle
st = turtle.Screen()
st.setup(630, 700, startx=400, starty=0)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 150)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 204:
        break
    t.hideturtle()
turtle.done()
