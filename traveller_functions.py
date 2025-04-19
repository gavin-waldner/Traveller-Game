import csv
import sys

def getHealth():
    with open ("health",'r') as hR:
        hNum = hR.read()
    print(f"Your current health is: {hNum}")
    return int(hNum)
    
def saveHealth(currentHealth):
    with open("health","w+") as hW:
        hW.write(str(currentHealth))
        
def takeDamage(dmg):
    with open("health",'r') as hR:
        hNum = hR.read()
        hNum = int(hNum)
        hNum -= dmg
    if hNum <= 0:
        print(f"You took {dmg} damage")
        print("You ran out of health. You died. Game over.")
        sys.exit(1)
    saveHealth(hNum)
    print(f"You took {dmg} damage")
        
    
def getRoad():
    with open ("road",'r') as rR:
        csv_reader = csv.reader(rR)
        for row in csv_reader:
            formatted_row = '|'.join(row)
            #print(formatted_row)
    return row

def printRoad():
    with open ("road",'r') as rR:
        csv_reader = csv.reader(rR)
        for row in csv_reader:
            formatted_row = '|'.join(row)
            print(formatted_row)
            
def saveRoad(cRoad):
    with open("road","w+", newline='') as rW:
        csv_writer = csv.writer(rW)
        csv_writer.writerow(cRoad)

def moveForward():
    cRoad = getRoad()
    cPos = cRoad.index('X')
    if cPos < 9:
        cRoad[cPos] = " "
        cRoad[cPos + 1] = "X"
        saveRoad(cRoad)
        
def moveBackward():
    cRoad = getRoad()
    cPos = cRoad.index('X')
    if cPos > 0:
        cRoad[cPos] = " "
        cRoad[cPos - 1] = "X"
        saveRoad(cRoad)
    else:
        cRoad
