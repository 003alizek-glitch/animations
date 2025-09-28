import turtle

# экран
s = turtle.Screen()
s.bgcolor("#303030")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# функция прямоугольника
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# функция звезды
def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)  # угол звезды
    t.end_fill()

# размеры
flag_width = 600
flag_height = 320
stripe_height = flag_height / 13
union_height = stripe_height * 7
union_width = flag_width * 0.4

# --- фон (красные и белые полосы) ---
for i in range(13):
    color = (178, 34, 52) if i % 2 == 0 else (255, 255, 255)
    draw_rectangle(-300, 160 - i*stripe_height, flag_width, stripe_height, color)

# --- синий прямоугольник (union) ---
draw_rectangle(-300, 160, union_width, union_height, (60, 59, 110))

# --- 50 звёзд ---
star_size = 12
start_x = -300 + 10
start_y = 160 - 10
row_spacing = union_height / 9
col_spacing = union_width / 6

for row in range(9):
    stars_in_row = 6 if row % 2 == 0 else 5
    offset_x = 0 if row % 2 == 0 else col_spacing / 2
    for col in range(stars_in_row):
        x = start_x + offset_x + col * col_spacing
        y = start_y - row * row_spacing
        draw_star(x, y, star_size, "white")

t.hideturtle()
turtle.done()
