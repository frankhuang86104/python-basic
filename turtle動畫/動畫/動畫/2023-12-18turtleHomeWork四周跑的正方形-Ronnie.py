import turtle

window = turtle.Screen()
window.colormode(255)
window.setup(width=600, height=400)
window.tracer(0)

#正方形邊長及牆壁位置
size = 50
window_top    = window.window_height()/2 - size/2   
window_bottom = -window.window_height() / 2 + size/2  
window_left   = -window.window_width() / 2 + size/2    
window_right  = window.window_width()/2 - size/2     

def 畫正方形(t1, length, color):
    t1.color(color)
    t1.penup()
    t1.setheading(270)
    t1.forward(length/2)
    t1.left(90)
    t1.forward(length/2)
    t1.left(90)
    t1.pendown()
    t1.begin_fill()
    for n in range(4):
        t1.forward(length)
        t1.left(90)
    t1.end_fill()

def 移動正方形(path, x, y, dx, dy, size):
    path.clear()
    path.goto(x, y)
    畫正方形(path, size, "cyan")

    if x >= window_right and dy == 0:
        x = window_right
        y = window_top
        dy = -0.3
        dx = 0

    elif dx==0 and y <= window_bottom:
        x = window_right
        y = window_bottom
        dx = -0.3
        dy = 0

    elif x <= window_left and dy == 0:
        x = window_left
        y = window_bottom
        dy = 0.3
        dx = 0

    elif dx == 0 and y >= window_top:
        x = window_left
        y = window_top
        dx = 0.3
        dy = 0
   
    x += dx
    y += dy

    return x, y, dx, dy

#產生烏龜
bob1 = turtle.Turtle()
bob1.shape("classic")
bob1.speed(10)
bob1.hideturtle()
bob1.penup()

size = 50
x = window_left
y = window_top
dx = 0.3
dy = 0

while True:  # 無窮迴圈
    x, y, dx, dy = 移動正方形(bob1, x, y, dx, dy, size)
    window.update()

window.exitonclick()