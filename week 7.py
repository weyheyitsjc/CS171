import turtle



def grass(x,y,h,w):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.color("green", "green",)
    turtle.begin_fill()
    for i in range(0,2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.end_fill()

def fence(x,y):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(12)
    turtle.left(90)
    turtle.forward(12)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()

def draw_fence(x,y):
    for i in range(0,16):
        fence(x,y)
        x+=25

def sun(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color("orange", "yellow")
    turtle.begin_fill()
    turtle.forward(70)
    turtle.left(36)
    turtle.end_fill()

def draw_sun(x, y):
    for i in range(0,10):
        sun(x, y)

    
    
grass(-200,-150,100,400)
draw_fence(-200,-150)
draw_sun(-200, 200)
