import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
who_is_it = "blue"
set_background("baseballfield")
s1 = create_sprite("blueguy (1)", 0,-200)
s2 = create_sprite("redguy (1)", 0, 200)
s2_tags=0
s1_tags=0
timer=0
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
 
def move_up():
    x = s2.xcor()
    y = s2.ycor() + 50
    s2.goto(x,y)
        
def move_down():
    x = s2.xcor()
    y = s2.ycor() - 50
    s2.goto(x,y)
    
def move_left():
    x = s2.xcor() - 50
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 50
    y = s2.ycor() 
    s2.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left,"Left")
window.onkeypress(move_right,"Right")
# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions
    if get_distance(s1,s2) < 100:
        if who_is_it == "blue":
            s1_tags += 1
            who_is_it = "red"
        elif who_is_it == "red":
            who_is_it = 1
            s2_tags += 1
            who_is_it = "blue"
        s2.write(f"tag {who_is_it} is it")
        s1.goto(0,-200)
        s2.goto(0,200)
        print (f"blues tags {s1_tags} reds tags {s2_tags}")
            # TODO - make an if statement for ending the game

    if i % 100 == 0:
        timer += 1
    if timer == 30:
        break
    time.sleep(0.01)
    window.update()
    

if s1_tags > s2_tags: 
    print ("blue wins!!")
elif s2_tags > s1_tags:
    print ("red wins!!")
elif s2_tags == s1_tags:
    print ("red wins!")
#the goal of the game is to get more tags than the other person but red just needs the tags to be equal because they always start with a one point defisate. 
print("Game Over")