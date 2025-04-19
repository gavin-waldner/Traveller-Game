from traveller_functions import *
from random import randint, seed
import csv

try:
    num = int(sys.argv[1])
except:
    print(f"Error: input argument ('{sys.argv[1]}') not a valid integer")
    sys.exit(1)
if len(sys.argv) == 2:
    seed_value = int(sys.argv[1])
    seed(seed_value)
elif len(sys.argv) > 2:
    print(f"Error: input argument ('{sys.argv[2]}') not a valid integer")
    sys.exit(1)
else:
    seed()
    sys.exit(1)


rW = open('road','w+',newline='')
# rR = open('road','r')
hW = open('health','w+')
# hR = open('health','r')

hW.write(str(100))
hW.close()

csv_writer = csv.writer(rW)
csv_writer.writerow(['X',' ',' ',' ',' ',' ',' ',' ',' ',' '])
#formatted_list = '|'.join(csv_writer)
rW.close()

getHealth()
printRoad()
print("Your journey begins. You are only at the first position.")
print("")
print("")


health = 100
placement = 0
while health > 0:
    print("")
    roll = randint(1,6)
    print('What will you do, traveller?')
    resp = input()
    if resp == "r" or resp == "p":
        print(f"You rolled a {roll}")
        if roll == 1:
            takeDamage(10)
        elif roll == 2:
            moveBackward()
            print("You moved back")
            placement = placement - 1
        elif roll == 3:
            newRoll = randint(1,10)
            if newRoll == 7:
                print("Salvation!!!")
                for i in range(9):
                    moveForward()
                print("You made it to the end of the road. Well done. You win!")
                sys.exit(1)
            else:
                print("Nobody heard your prayers")
        elif roll == 4:
            takeDamage(40)
        elif roll == 5:
            placement
        elif roll == 6:
            moveForward()
            print("You moved forward")
            placement = placement + 1
        if placement < 0:
            placement = 0
        getHealth()
        printRoad()
        print("")
        print("")
    elif resp == "q":
        sys.exit(1)
    else:
        print("Invalid Selection. Please choose to either:")
        print("\tr - roll the dice")
        print("\tp - consume a potion")
        print("\tq - quit")
