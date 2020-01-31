import turtle

def jump(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def cantor(x,y,size):
    if size > 1:
        jump(x,y)
        turtle.forward(size)
        space = 4
        nsize = size/2 - space/2
        cantor(x,y+space,nsize)
        cantor(x+space+nsize, y+space,nsize)
    
#cantor(-100, 0, 300)
        
def square(x,y,size):
    jump(x-size/2,y+size/2)
    turtle.color("red", "blue")
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    
def carpet(x,y,size):
    if size > 2:
        square(x,y,size)
        nsize = size/3
        carpet(x+size,y,nsize)
        carpet(x-size, y, nsize)
        carpet(x, y+size, nsize)
        carpet(x, y-size, nsize)
        carpet(x+size, y+size, nsize)
        carpet(x+size, y-size, nsize)
        carpet(x-size, y+size, nsize)
        carpet(x-size, y-size, nsize)
        
turtle.speed(0)
carpet(0,0,300)