import random
from globalvars import * 

## Functions
def displayMarketPositions():   
    global marketValueArray, elementMarketDict
    print("Current Market")
    headerString = "| "
    valueString = "| "

    for key, val in elementMarketDict.items():
        marketPosition = val if val<= 9 else 9
        headerString = f'{headerString}{key.title().ljust(10)} | '
        valueString = f'{valueString}{str(marketValueArray[marketPosition]).ljust(10)} | '
    
    print(headerString)
    print(valueString)
    print("\n")

def updateAndDisplayMarketPositions():
    global elementMarketDict, marketDice
    dOne = marketDice[0]-1
    dTwo = marketDice[1]-1
    dThree = marketDice[2]-1
    elementMarketDict[elementMarketKeys[dOne]] = elementMarketDict[elementMarketKeys[dOne]]+ 1
    elementMarketDict[elementMarketKeys[dTwo]] = elementMarketDict[elementMarketKeys[dTwo]] + 1
    elementMarketDict[elementMarketKeys[dThree]] = elementMarketDict[elementMarketKeys[dThree]] + 1
    displayMarketPositions()

def dieRoll(type, die):
    type[die] = random.randint(1, 6)

def rollThree(type):
    dieRoll(type, 0)
    dieRoll(type, 1)
    dieRoll(type, 2)


def comboCalc(x, y):
    global roomArray, lastRoom
    stopOne = (lastRoom + x) % 13
    stopTwo = (stopOne + y) % 13
    print(f'{roomArray[(stopOne-1)]}, {roomArray[(stopTwo-1)]}')


def roomCalculator():
    global lastRoom, roomDice
    a = roomDice[0]
    b = roomDice[1]
    c = roomDice[2]
    totalSteps = a + b + c
    print(f'A:{a}  B:{b}  C:{c}')
    comboCalc(a, b)
    comboCalc(a, c)
    comboCalc(b, a)
    comboCalc(b, c)
    comboCalc(c, a)
    comboCalc(c, b)
    lastRoom = (lastRoom + totalSteps) % 13
    return lastRoom