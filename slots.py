import random
import os
import time

slotOptions = [1, 2, 3]
balance = 1000

# Clear the command prompt screen based on OS
def clearScreen():
    if (os.name == 'nt'):
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')

while True:
    # Quit game loop once user has no money left
    if balance == 0:
        print('You have no money left, Game Over')
        break

    print('How much do you want to gamble? Your balance is ' + str(balance))
    gamble = input()
    clearScreen()

    if (gamble.isdigit() == True):
        if (int(gamble) > balance):
            print('Insufficient balance')
        else:
            slotOne = random.choice(slotOptions)
            slotTwo = random.choice(slotOptions)
            slotThree = random.choice(slotOptions)

            # 'Animate' slots
            for i in range(0, 5):
                clearScreen()
                print('[' + str(random.choice(slotOptions)) + '] [' + str(random.choice(slotOptions)) + '] [' + str(random.choice(slotOptions)) +']')
                time.sleep(0.2)

            clearScreen()
            print('[' + str(slotOne) + '] [' + str(slotTwo) + '] [' + str(slotThree) +']')

            # Recalculate balance based on win/loss
            if (slotOne == slotTwo and slotTwo == slotThree):
                # Prize calculated by slot number * gamble value
                wins = int(slotOne) * int(gamble)
                balance += int(slotOne) * int(gamble)
                print('Congratulations you have won ' + str(wins) + ' credits!')
            else: 
                balance = balance - int(gamble)
                print('Oh no, you have lost ' + gamble + ' credits')