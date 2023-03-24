from functions import *

## Phases
def setUpPhase():
    global lastRoom, singleDie, marketDice, roomArray
    #print("Set Up Phase")
    rollThree(marketDice)
    dieRoll(singleDie, 0)
    #print(f'''Die One: {marketDice[0]}, Die Two: {marketDice[1]}, Die Three: {marketDice[2]}, Die Four: {singleDie[0]}''')
    #print("Starting Market")
    updateAndDisplayMarketPositions()
    lastRoom = singleDie[0]
    print(f'Starting Room: {roomArray[(lastRoom-1)]}')

def roomPhase():
    global roomDice, roomArray
    #print("Building Phase")
    rollThree(roomDice)
   # print(f'''Room Roll:Die One: {roomDice[0]}, Die Two: {roomDice[1]}, Die Three: {roomDice[2]}''')
    #print("Current Market")
    #displayMarketPositions()
    newRoomPos = roomCalculator() -1    
    print(f'Phase Ending Room: {roomArray[newRoomPos]}\n')    
    # displayMarketPositions()

def marketPhase():
    global marketDice
    #print("Market Phase")
    rollThree(marketDice)
    print(f'X:{marketDice[0]}  Y:{marketDice[1]}  Z:{marketDice[2]}')
    #print(f'''Market Roll:Die One: {marketDice[0]}, Die Two: {marketDice[1]}, Die Three: {marketDice[2]}''')
    updateAndDisplayMarketPositions()