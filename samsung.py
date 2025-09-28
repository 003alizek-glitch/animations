from turtle import *
tracer(2)
bgcolor("black")
pencolor("white")
pensize(3)
def Goto(x, y):
    penup()
    goto(x, y)
    pendown()
Goto(-100, 260)

def galaxy(x, y):
    for i in range(2):
        fd(x)
        for i in range(90):
            fd(0.05)
            rt(1)
        fd(y)
        for i in range(90):
            fd(0.05)
            rt(1)

begin_fill()
pencolor("#97822d")
fillcolor("#f3d64e")
galaxy(240, 500)
end_fill()
Goto(-90, 240)

def camera(f,c):
    begin_fill()
    fillcolor(c)
    for i in range(360):
        fd(f)
        rt(1)
    end_fill()
Goto(-60, 240)
camera(0.37, "#000000")
Goto(-60, 185)
camera(0.37, "#000000")
Goto(-60, 130)
camera(0.37, "#000000")
pensize(2)
Goto(-9, 231)
camera(0.19, "#000000")
Goto(-9, 176)
camera(0.19, "#000000")
pencolor("#f5f4d1")
Goto(-9, 197)
camera(0.07, "#f5f4d1")
hideturtle()

# SAMSUNG
Goto(-25, -150)
color("#97822d")
style = ("arial", 10, "bold")
write("S A M S U N G", font=style)
done()