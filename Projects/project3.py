
import turtle, time, random
from utils import *


for i in range(10):
     
     
    # Section 1 - Variables
    # TODO - add starting values for all the variables
     x1 =-200
     y1 =100
     x2 =-200
     y2 =-0
     x3 =-200
     y3 =-100
     x4 =-200
     y4 =-200


    # Section 2 - Setup
    # TODO - use your own background, and set your four turtles to images of your choice
     set_background("barn")
     t1 = create_sprite("alien",x1,y1)
     t2 = create_sprite("fish",x2,y2)
     t3 = create_sprite("cat2",x3,y3)
     t4 = create_sprite("dog",x4,y4)


    # Section 3 - Racing
    # on average t2 will win the most but any of them can win
     for i in range(30):
        x1 +=15
        x2 +=random.randint(10,30)
        x3 +=random.randint(1,35)
        x4 +=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,500])

        t1.goto(x1, y1)
        t2.goto(x2, y2)
        t3.goto(x3, y3)
        t4.goto(x4, y4)

        window.update()
        time.sleep(0.3)


    # Section 4 - Winner
    # TODO - complete the elif for player 2 winning
    # TODO - write another elif for player 3 and player 4
     if x1 >= x2 and x1 >= x3 and x1 >= x4:
        print("player 1 wins!")
     elif x2 >= x1 and x2 >= x3 and x2 >= x4:
         print("player 2 wins!")
         
     elif x3 >= x2 and x3 >= x1 and x3 >= x4:
         print ("player 3 wins!")
         
     elif x4 >= x2 and x4 >= x3 and x4 >= x1:
         print ("player 4 wins!")
         
    
turtle.exitonclick()
