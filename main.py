from phases import *

def main():
    print("\n")
    setUpPhase()

    i = 0
    while i < 8:
        roomPhase()
        roomPhase()  
        ## Market phase could be called earlier with the use of the predictor room
        marketPhase()
        i = i+1
    
    roomPhase()    
    # print('\nFinal Market Value')
    # displayMarketPositions()

if __name__ == "__main__":
    main()