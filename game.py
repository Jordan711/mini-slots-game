from slots import *

# Create a new slot machine before starting the game
slotMachine = SlotMachine()

while True:
    if (slotMachine.balanceIsZero() == False):
        if (slotMachine.getGambleAmount() == True):
            slotMachine.animateSlotRoll()
            [slotOne, slotTwo, slotThree] = slotMachine.rollSlots()
            print(slotMachine.calculateWinLoss([slotOne, slotTwo, slotThree]))
        else: 
            slotMachine.clearScreen()
            print('Invalid input, please check you have sufficient funds')
            pass
    else:
        print('You have insufficient funds to play. Game Over')
        break