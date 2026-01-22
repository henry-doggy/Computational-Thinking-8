basketball_points = 0
soccer_points = 0
skiing_points = 0

answer1 = input ("do you like winter, A or spring,B? "   )
if answer1 == "A" or "a":
    basketball_points += 1
    skiing_points += 1
elif answer1 == "B":
    soccer_points += 1
answer2 = input ("what type of sports do you like watching A, Xgames, B, indoor Sports, or C, outdoor sports, ")
if answer2 == "A": 
    skiing_points +=1
elif answer2 == "B":
    basketball_points += 1
elif answer2 == "C":
    soccer_points += 1
Answer3 = input ("Do you A, ,prefer the snow or B, prefer the sun? ")
if Answer3 == "A":
    skiing_points += 1
elif Answer3 == "B":
    soccer_points += 1
    basketball_points += 1
answer4 = input ("if it was snowing would you A, go outside and play, B, stay inside and play basket ball, or C, go and play soccer? ")
if answer4 == "A":
    skiing_points += 1
elif answer4 == "B":
    basketball_points += 1
elif answer4 == "C":
    soccer_points += 1
answer5 = input ("are you canadian? A for yes and B for no ")
if answer5 == "A" or "a":
    skiing_points += 1

    soccer_points += 1
    basketball_points += 1
if basketball_points > skiing_points and basketball_points > soccer_points:
    print("oh nice! you like basket ball! if you wanted to get skiing you could put A,A,A,A")
elif skiing_points > soccer_points and skiing_points > basketball_points:
    print ("oh cool you like skiing, nice choice! if you wanted the soccer answer you could put B,C,B,C,B")
elif soccer_points > skiing_points and soccer_points > basketball_points:
    print("oh! you like soccer, cool! if you wanted the basket ball answer you could put A,B,B,B,B")