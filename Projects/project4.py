import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("icreamshopbackround")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
icecream = 0
cost = 0
machines = 0

# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -300,200)
message_sprite.hideturtle()
# creat_sprite("alien", -200,200)
# create_sprite.hideturtle()


# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_icecream():
    global icecream
    icecream += 1
    x = random.randint(-400,400)
    y = random.randint(-200,200)
    create_sprite ("icecream (1).gif", x, y)
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_icecream, "space")
# TODO - make a second    control
def buy_machine():
    global icecream, machines
    y = 100 +20* machines
    x = 100 
    create_sprite("image.gif")
    if icecream >= 10:
        machines += 1
        icecream -= 10
window.onkeypress(buy_machine, "m")



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    if i % 100 == 0 :
        
        icecream += machines 

    #the goal is to get as much icecream as posible
    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.color("white")
    message_sprite.write(f"icecream: {icecream}  machines: {machines}",font= ("Arial", 20, "normal"))
    
    time.sleep(0.01)
    window.update()