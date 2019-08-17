import random
from collections import Counter

def goldRandomizer(value):
    hiValue = value + (value*0.1)
    minValue = value - (value*0.1)
    return random.randint(minValue,hiValue)

# set up of the random variables
gameLenght = 0
# boxes kinds [random percentage, gold inside]
greenBox = [60,1000]
orangeBox = [25,4000]
violetBox = [10,9000]
legendaryBox = [5,16000]
# chance to drop a box
boxChance = 60
# names of the boxes
boxes = ['Green','Orange','Violet','Legendary']
# player set up
playerGold = []
print('Welcome in lootbox simulator')
playerName = input('Please enter your name: ')
while True:
    try:
        howManyMoves = int(input('Enter the number of moves do you want to make: '))
        break
    except:
        print('It have to be a number....')
        continue
boxesFound = []
counter = 0
errorCounter = 0
while gameLenght<howManyMoves:
    boxChanceHit = random.randint(1,100)
    if boxChanceHit<=boxChance:
        # print('You found a box!')
        counter+=1
        lottery = random.choices(boxes, [greenBox[0], orangeBox[0], violetBox[0], legendaryBox[0]], k=100)
        ticket = random.randint(0,99)
        if lottery[ticket] == 'Green':
            playerGold.append(goldRandomizer(greenBox[1]))
            print('You found a Green box! Now you have',sum(playerGold),'gold')
            boxesFound.append(lottery[ticket])
        elif lottery[ticket] == 'Orange':
            playerGold.append(goldRandomizer(orangeBox[1]))
            print('You found a Orange box! Now you have',sum(playerGold),'gold')
            boxesFound.append(lottery[ticket])
        elif lottery[ticket] == 'Violet':
            playerGold.append(goldRandomizer(violetBox[1]))
            print('You found a Violet box! Now you have',sum(playerGold),'gold')
            boxesFound.append(lottery[ticket])
        elif lottery[ticket] == 'Legendary':
            playerGold.append(goldRandomizer(legendaryBox[1]))
            print('You found a Violet box! Now you have',sum(playerGold),'gold')
            boxesFound.append(lottery[ticket])
        else:
            print('ERROR!!!',lottery[ticket])
            errorCounter+=1
    gameLenght += 1
print('Congratulations',playerName,'!!! \nYou found',counter,'boxes!')
print('You have aquired',sum(playerGold),'gold!')
print(Counter(boxesFound))
print(errorCounter,'errors founded')
input('Press enter to end program')
