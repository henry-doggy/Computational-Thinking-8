# Section 1 - Your code
from utils import *
set_background("soccerfield")

s1 = create_sprite("soccerball", 50, 100)
s2 = create_sprite("character1", 51, -100)

message1 = create_sprite("alien",-200,100)
message1.color("Purple")
message1.write("GOAALLLLLLL",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()