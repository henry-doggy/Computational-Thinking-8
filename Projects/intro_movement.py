import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 50
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 50
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 50
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 50
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left,"a")
window.onkeypress(move_right,"d")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide,"f")
window.onkeyrelease(show, "f")

def draw():
    s1.pendown()
window.onkeypress(draw, "c")

def stop_drawing():
    s1.penup()
window.onkeypress(stop_drawing, "q")

def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "e")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "r")

def reset():
    s1.goto(0,0)
window.onkeypress(reset, "space")





# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()