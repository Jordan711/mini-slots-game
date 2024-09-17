from slots import *

# GAME PARAMS: Change to your preference
initialStartingBalance = 1000
slotOptions = [5, 6]

# Create a new slot machine before starting the game
slotMachine = SlotMachine(balance=initialStartingBalance, slotOptions=slotOptions)

while True:
    if (slotMachine.balanceIsZero() == False):
        if (slotMachine.getGambleAmount() == True):
            slotMachine.animateSlotRoll()

            [slotOne, slotTwo, slotThree] = slotMachine.rollSlots()
            slotMachine.clearScreen()
            print('[' + str(slotOne) + '] [' + 
                  str(slotTwo) + '] [' + 
                  str(slotThree) +']')
            
            print(slotMachine.calculateWinLoss([slotOne, slotTwo, slotThree]))
        else: 
            slotMachine.clearScreen()
            print('Invalid input, please check you have sufficient funds')
            pass
    else:
        print('You have insufficient funds to play. Game Over')
        break