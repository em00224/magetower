## Market Global Variables
marketValueArray = [-2, -1, 0, 1, 2, 1, 0, -1, -2, -3]
elementMarketDict = {
    'light': 0,
    'fire': 0, 
    'air': 0,
    'water': 0, 
    'earth': 0,
    'dark': 0
}
elementMarketKeys = list(elementMarketDict)

## Dice Global Variables
singleDie = [0]
roomDice = [0, 0, 0]
marketDice = [0, 0, 0]

## Room Global Variables
roomArray = ['light', #1
             'fire', #2
             'air', #3
             'water', #4
             'earth', #5
             'dark', #6
             'explosion', #7 
             'labratory', #8
             'predictor', #9
             'distorter', #10
             'tower cap', #11
             'gryphon nest', #12
             'explosion'] #13
lastRoom = 0
specialRooms = ['library', 'staircase']

placedRooms = []
crossedOutRooms = []