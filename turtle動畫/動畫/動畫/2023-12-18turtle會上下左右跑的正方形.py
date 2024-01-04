import turtle

window = turtle.Screen()
window.colormode(255)
window.setup(width=600, height=400)
window.tracer(0)

def 畫正方形(t1 , length , color) :
    t1.color(color)
    t1.setheading(270)
    t1.forward(length/2)
    t1.left(90)
    t1.forward(length/2)
    t1.left(90)
    t1.pendown()
    t1.begin_fill()
    for n in range(4) :
        t1.forward(length)
        t1.left(90)
    t1.end_fill()
    t1.penup()
    return print("畫好了")

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(10)
bob1.hideturtle()
bob1.penup()

length = 50
x = -window.window_width()/2+length/2  # -275
y = window.window_height()/2-length/2
dx = 0.3
dy=0.3
while True : # 無窮迴圈

    bob1.clear()
    bob1.goto(x,y)
    畫正方形(bob1,length,"red")

    if x > window.window_width()/2-length/2 :  # 275
        dx = -dx
    if x < -window.window_width()/2+length/2 : # -275
        dx = -dx
    x += dx

    if y > window.window_height()/2-length/2 :  # 175
        dy = -dy
    if y < -window.window_height()/2+length/2 : # -175
        dy = -dy
    y += dy
    window.update()

window.exitonclick()