import random      #imports random module
p1c = 0            #Assignment of scoring values
p2c = 0
p3c = 0
p4c = 0
def pointplus():     #Function for addition of points
    if (p == 1):
        global p1c
        p1c += 1
    elif (p == 2):
        global p2c
        p2c += 1
    elif (p == 3):
        global p3c
        p3c += 1
    else:
        global p4c
        p4c += 1
def pointminus():    #Function for reduction of points
    if (p == 1):
        global p1c
        p1c -= 1
    elif (p == 2):
        global p2c
        p2c -= 1
    elif (p == 3):
        global p3c
        p3c -= 1
    else:
        global p4c
        p4c -= 1
def exit():
    raise Exception('exit')
def frscharname():       #Checks First Character
    firstchar = name[0]
    if (firstchar != lft[0]):
        print('Wrong Letter!')
        pointminus()
    else:
        print()
def frscharplace():       #Checks First Character
    firstchar = place[0]
    if (firstchar != lft[0]):
        print('Wrong Letter!')
        pointminus()
    else:
        print()
def frscharanimal():      #Checks First Character
    firstchar = animal[0]
    if (firstchar != lft[0]):
        print('Wrong Letter!')
        pointminus()
    else:
        print()
def frscharthing():         #Checks First Character
    firstchar = thing[0]
    if (firstchar != lft[0]):
        print('Wrong Letter!')
        pointminus()
    else:
        print()
def vername():             #Reads and Writes File data
    with open('files/namec.txt') as file:
        contents = file.read()
        if name in contents:
            print ('Verified!')
            pointplus()
        else:
            vryn = input('Do you verify that this input is correct? y/n')
            vryn = vryn.upper()
            if (vryn == 'Y'):
                nametext = open('namec.txt',"a")
                nametext.write('\n')
                nametext.write(name)
                nametext.close()
                pointplus()
            else:
                print(-1)
                pointminus()
def verplace():           #Reads and Writes File data
    with open('files/placec.txt') as file:
        contents = file.read()
        if place in contents:
            print ('Verified!')
            pointplus()
        else:
            vryn = input('Do you verify that this input is correct? y/n')
            vryn = vryn.upper()
            if (vryn == 'Y'):
                placetext = open('placec.txt',"a")
                placetext.write('\n')
                placetext.write(place)
                placetext.close()
                pointplus()
            else:
                print(-1)
                pointminus()
def veranimal():             #Reads and Writes File data
    with open('files/animalc.txt') as file:
        contents = file.read()
        if name in contents:
            print ('Verified!')
            pointplus()
        else:
            vryn = input('Do you verify that this input is correct? y/n')
            vryn = vryn.upper()
            if (vryn == 'Y'):
                animaltext = open('animalc.txt',"a")
                animaltext.write('\n')
                animaltext.write(animal)
                animaltext.close()
                pointplus()
            else:
                print(-1)
                pointminus()
def verthing():               #Reads and Writes File data 
    with open('files/thingc.txt') as file:
        contents = file.read()
        if name in contents:
            print ('Verified!')
            pointplus()
        else:
            vryn = input('Do you verify that this input is correct? y/n')
            vryn = vryn.upper()
            if (vryn == 'Y'):
                thingtext = open('thingc.txt',"a")
                thingtext.write('\n')
                thingtext.write(thing)
                thingtext.close()
                pointplus()
            else:
                print(-1)
                pointminus()
abcleft = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
abcused = []                      #For future game updates :)
lft = random.choice(abcleft)
alreadyused = []
player = int(input('How many players? 2-4'))
if (player > 4 or player < 2):
    exit()
for i in range(len(abcleft)):        #For entire alphabet
    for i in range(player):           #No of players
        p = i + 1                     #identifier of player
        print('Player',p,'Please Enter A Name That Starts With The Letter',lft)
        name = input(':')
        name = name.upper()
        frscharname()
        if (name in alreadyused):
            print("You can't repeat what has already been said!!!")
            pointminus()
        else:
            vername()
            alreadyused.append(name)
        print('Player',p,'Please Enter A Place That Starts With The Letter',lft)
        place = input(':')
        place = place.upper()
        frscharplace()
        if (place in alreadyused):
            print("You can't repeat what has already been said!!!")
            pointminus()
        else:
            verplace()
            alreadyused.append(place)
        print('Player',p,'Please Enter An Animal That Starts With The Letter',lft)
        animal = input(':')
        animal = animal.upper()
        frscharanimal()
        if (animal in alreadyused):
            print("You can't repeat what has already been said!!!")
            pointminus()
        else:
            veranimal()
            alreadyused.append(animal)
        print('Player',p,'Please Enter A Thing That Starts With The Letter',lft)
        thing = input(':')
        thing = thing.upper()
        frscharthing()
        if (thing in alreadyused):
            print("You can't repeat what has already been said!!!")
            pointminus()
        else:
            verthing()
            alreadyused.append(thing)
        lft = lft.upper()
        abcused.append(lft)
    p = 0                               #resets player value
    lft = random.choice(abcleft)
    cont = input('Would you like to continue? Y/N')
    cont = cont.upper()
    if cont == 'N':
        break                            #cuts straight to player score     
print('Player 1 score',p1c)
print('Player 2 score',p2c)
print('Player 3 score',p3c)
print('Player 4 score',p4c)
