import random
import os
import time

slotOptions = [1, 2, 3, 4, 5, 6]
balance = 1000

while True:
    if balance == 0:
        print('You have no money left, Game Over')
        break

    print('How much do you want to gamble? Your balance is ' + str(balance))
    gamble = input()
    if (os.name == 'nt'):
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')

    if (gamble.isdigit() == True):
        if (int(gamble) > balance):
            print('Insufficient balance')
        else:
            slotOne = random.choice(slotOptions)
            slotTwo = random.choice(slotOptions)
            slotThree = random.choice(slotOptions)

            for i in range(0, 5):
                if (os.name == 'nt'):
                    os.system('cls')
                elif (os.name == 'posix'):
                    os.system('clear')
                print('[' + str(random.choice(slotOptions)) + '] [' + str(random.choice(slotOptions)) + '] [' + str(random.choice(slotOptions)) +']')
                time.sleep(0.3)
            if (os.name == 'nt'):
                os.system('cls')
            elif (os.name == 'posix'):
                os.system('clear')
            print('[' + str(slotOne) + '] [' + str(slotTwo) + '] [' + str(slotThree) +']')

            if (slotOne == slotTwo and slotTwo == slotThree):
                wins = int(slotOne) * int(gamble)
                balance += int(slotOne) * int(gamble)
                print('Congratulations you have won ' + str(wins) + ' credits!')
            else: 
                balance = balance - int(gamble)
                print('Oh no, you have lost ' + gamble + ' credits')