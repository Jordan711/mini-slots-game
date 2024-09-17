import random
import os
import time

class SlotMachine:
    def __init__(self, balance=1000, slotOptions=[1, 2, 3]):
        self.balance = balance
        self.slotOptions = slotOptions
        self.gamble = 0
    
    def clearScreen(self):
        '''
        Clears the screen of text using commands
        based on its operating system

        (self) -> None
        '''
        if (os.name == 'nt'):
            os.system('cls')
        elif (os.name == 'posix'):
            os.system('clear')
    
    def balanceIsZero(self):
        '''
        Returns a boolean that determines if balance is zero or not

        (self) -> Boolean
        '''
        if (self.balance == 0):
            return True
        else:
            return False

    def getGambleAmount(self):
        '''
        Get input from the user and do error checking
        Return boolean based on whether gamble amount
        is saved successfully

        (self) -> Boolean
        '''
        print('How much do you want to gamble? Your balance is ' + str(self.balance))
        userInput = input()
        if (userInput.isdigit() == False) or (int(userInput) > self.balance):
            return False
        else:
            self.gamble = userInput
            return True
    
    def rollSlots(self):
        '''
        Returns a list of randomly selected slot values

        (self) -> [Int, Int, Int]
        '''
        slotOne = random.choice(self.slotOptions)
        slotTwo = random.choice(self.slotOptions)
        slotThree = random.choice(self.slotOptions)
        return [slotOne, slotTwo, slotThree]

    def animateSlotRoll(self):
        '''
        Create a sequence of clear screens, and printing
        random slot values

        (self) -> None
        '''
        for i in range(0, 5):
            self.clearScreen()
            print('[' + str(random.choice(self.slotOptions)) + '] [' + 
                  str(random.choice(self.slotOptions)) + '] [' + 
                  str(random.choice(self.slotOptions)) +']')
            time.sleep(0.2)

    def calculateWinLoss(self, slotRoll):
        '''
        Calculate the win/loss amount based on the slot values
        and returns the message to be printed

        (self, [Int, Int, Int]) -> String
        '''
        # Recalculate balance based on win/loss
        if (slotRoll[0] == slotRoll[1] and slotRoll[1] == slotRoll[2]):
            # Prize calculated by slot number * gamble value
            wins = int(slotRoll[0]) * int(self.gamble)
            self.balance += int(slotRoll[0]) * int(self.gamble)
            return 'Congratulations you have won ' + str(wins) + ' credits!'
        else: 
            self.balance = self.balance - int(self.gamble)
            return 'Oh no, you have lost ' + self.gamble + ' credits'

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
