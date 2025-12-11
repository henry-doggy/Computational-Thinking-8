name = input("what is your name? ")
print(f"Hello {name}!")
mood = input("how are you feeling today? ")
if mood == "sad": 
    print(f"oh sorry,")
    print("I hope you fell better")
else: 
    print(f"oh nice,") 
    print(f"im also feeling {mood} today!")
answer1 = input("do you have any pets? (yes/no) ")
if answer1 == "yes": 
    pet = input (f"oh cool! what is it? ")
    print(f"nice!") 
    print(f"ive always wanted {pet}")
else:
    print (f"that sucks!")
