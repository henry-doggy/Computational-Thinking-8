input ("you are poor and need money")
input("so you decide to go to the mines and try to find diamands")
input("so you go to the store for some suplies")
input("you up to the guy in the shop and he offers you 2 things")
tool1 = input ("do you want the tnt or the pickaxe? ")
if tool1 == "tnt" or "the tnt":
    print("the tnt explodes on your way out of the store and you die")
if tool1 == "pickaxe" or "The pickaxe":
    print(f"you walk to the mines with your new {tool1}")
    input("when you get to the mines there is an old man with a long beard")
    input("he says you have to solve a riddle to get past")
    answer1 = input("Poor people have it, rich people need it. If you eat it, you'll die. What is it? ")
    if answer1 == "nothing":
        print("your correct!")
        input("you continue into the mines")
        input("you come across 3 stones")
        stone1 = input("which one do you brake? (1,2, or 3) ")
        if stone1 == "1":
            input("you found dimands!")
            print("you win!!!!")
        if stone1 == "2":
            input("a monster jumps out and kiils u")
            print("you lose!!!")
        if stone1 == "3":
            input("theres nothing so you continue into the cave")
            input("you been walking for 3 hours know,")
            input("and you come acrosse a sword next to a metal door")
            answer2 = input("do you wish to pick up the sword and go in? ")
            if answer2 == "yes":
                input("you walk in to the room and find a monster")
                fight1 = input ("do you try to hit its leg or arm? ")
                if fight1 == "its leg" or "leg":
                    print("you cut its leg of and it falls down and dies")
                    input("and it explodes into diamands and gold!!")
                    print("you win!!")
                if fight1 == "arm" or "its arm":
                    input("you miss and its kills you")
                    input("you lose!!")


        
    else:
        print("you arnt alowed in and never find dimands")

