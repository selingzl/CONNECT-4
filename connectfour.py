import os
import random

turnCounter = 0

f = open("tahta.txt", "a")
h = open("hamle.txt", "a")

moon = "\U0001F31A"
sun = "\U0001F31E"

print("Welcome to Connect 4 Game: ")
print("----------------------------")
print("\n Chips are moon: ", "\U0001F31A", "and sun: ", "\U0001F31E")

print("\n Please enter 1. player's name:")

first_name = input("name: ")
                
print("Please enter 2. player's name:")

second_name = input("name: ")

names = [first_name, second_name]

x = random.choice(names)

print(x)

if (x == first_name):
    first_chip = sun
    second_chip = moon
else:
    first_chip = moon
    second_chip = sun
   
print(first_chip)

firstplayer = first_name 
f.write(firstplayer)
secondplayer = second_name 
f.write(secondplayer)

players = {
    first_chip : first_name,
    second_chip : second_name
}

def menu(x,f,h):
    if (f.readline() + "boş" == "boş" and x == "CONTINUE"):
        print("There is not existing any game. You should create a new one")
        x = input("enter: ")

    elif (f.readline() + "boş" != "boş" and x == "CONTINUE"):
        continueGame(h)
        pickedSpace = input("\n Choose a space: ")
    
    if(x == "NEW GAME"):
        deModifyArray()
        
        f.close()
        h.close()
        
        os.remove("tahta.txt")
        os.remove("hamle.txt")
        
        f = open("tahta.txt", "a+")
        h = open("hamle.txt", "a+")
       
        print("\n Chips are moon: ", "\U0001F31A", "and sun: ", "\U0001F31E")

        print("\n Please enter 1. player's name:")

        first_n = input("name: ")
                        
        print("Please enter 2. player's name:")
        
        second_n = input("name: ")
        
        names = [first_n, second_n]
        
        x = random.choice(names)
        
        if x == first_n:
            first_c = sun
            second_c = moon
        else:
            first_c = moon
            second_c = sun
   
            
        firstplay = first_n 
        f.write(firstplay)
        secondplay = second_n 
        f.write(secondplay)
        
        newplayers ={
            first_c : first_n,
            second_c :second_n
        }
        
        players.update(newplayers)
    

Letters = ["A","B","C","D","E","F","G","H","J"]
rows=9
cols=9
gameboard = [["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""]]



def printGameBoard():
    print("\n     A    B    C    D    E    F    G    H    J", end ="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+----+----+")
        print(x," |", end ="")
        for y in range(cols):
                if (gameboard[x][y] == moon):
                    print("", gameboard[x][y], end = " |")
                elif (gameboard[x][y] == sun):
                    print("", gameboard[x][y], end = " |")
                else:
                    print(" ", gameboard[x][y], end = "  |")
    print("\n   +----+----+----+----+----+----+----+----+----+")

def modifyArray(pickedSpace, turn):
    gameboard[pickedSpace[0]][pickedSpace[1]] = turn

def deModifyArray():
    turn = ""
    for i in range(0,9):
        for j in range(0,9):
            gameboard[i][j] = turn


def checkWinner(chip):
    #check the horizontal spaces
    for y in range(rows):
        for x in range(cols - 3):
            if(gameboard[x][y] == chip and gameboard[x+1][y] == chip and gameboard[x+2][y] == chip and gameboard[x+3]
                [y] == chip):
                print("\n Game Over!", players.get(chip) , " wins, thanks for playing :)")
                return True
     
     #check the vertical spaces
    for x in range(rows):
        for y in range(cols - 3):
            if(gameboard[x][y] == chip and gameboard[x][y+1] == chip and gameboard[x][y+2] == chip and gameboard[x]
                [y+3] == chip):
                print("\n Game Over!", players.get(chip) , " wins, thanks for playing :)")
                return True
    
    #check the diagonal spaces (top right to bottom left)
    for x in range(rows - 3):
        for y in range(3, cols):
            if(gameboard[x][y] == chip and gameboard[x+1][y-1] == chip and gameboard[x+2][y-2] == chip and gameboard[x+3][y-3] == chip):
                print("\n Game Over!", players.get(chip) , " wins, thanks for playing :)")
                return True
    
    #check the diagonal spaces (top left to bottom right)
    for x in range(rows - 3):
        for y in range(cols - 3):
            if(gameboard[x][y] == chip and gameboard[x+1][y+1] == chip and gameboard[x+2][y+2] == chip and gameboard[x+3][y+3] == chip):
                print("\n Game Over!", players.get(chip) , " wins, thanks for playing :)")
                return True
    
    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if(inputString[0] == "A"):
        coordinate[1] = 0
    elif(inputString[0] == "B"):
        coordinate[1] = 1
    elif(inputString[0] == "C"):
        coordinate[1] = 2
    elif(inputString[0] == "D"):
        coordinate[1] = 3
    elif(inputString[0] == "E"):
        coordinate[1] = 4
    elif(inputString[0] == "F"):
        coordinate[1] = 5
    elif(inputString[0] == "G"):
        coordinate[1] = 6
    elif(inputString[0] == "H"):
        coordinate[1] = 7
    elif(inputString[0] == "J"):
        coordinate[1] = 8
    else:
        print("\n invalid")

    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(iCoordinate):
    if(gameboard[iCoordinate[0]][iCoordinate[1]] == sun):
        return False
    elif(gameboard[iCoordinate[0]][iCoordinate[1]] == moon):
        return False
    else:
        return True
    
def gravityChecker(iCoordinate):
    
    #calculate space below
    spaceBelow = [None] * 2
    spaceBelow[0] = iCoordinate[0] + 1
    spaceBelow[1] = iCoordinate[1] 
    
    #is the coordinate at ground level
    if(spaceBelow[0] == 9):
        return True 
    
    #check if there is a token below
    if(isSpaceAvailable(spaceBelow) == False):
        return True
    
    return False

turnCounter = 0
print("If you want to quit press Q")

def continueGame(h):
    Lines = h.readlines()
    for i in Lines:
        coordinateParser(i)
        
    printGameBoard()


moon_array = []
sun_array = []


f.close()
h.close()

while True:
    if(turnCounter % 2 == 0):
        printGameBoard()
        print("\n", players.get(moon), " plays")
        while True:
            pickedSpace = input("\n Choose a space or press Q: ")
        
            if pickedSpace != "Q" :
                moon_array.append(pickedSpace)
               
                coordinate = coordinateParser(pickedSpace)
                
                f = open("tahta.txt","a")
                h = open("hamle.txt","a")
                
                tahta =  pickedSpace
                f.write(tahta)

                h.write(moon_array[turnCounter % 2 - 1])
                
               
            else:
                print("Game stopped")
                print("Welcome to Connect 4 Game: ")
                print("----------------------------")
                x = input("Please enter NEW GAME or CONTINUE: ")
                
                f = open("tahta.txt","r+")
                h = open("hamle.txt", "r+")
                
                menu(x,f,h)
                f = open("tahta.txt","r")
                if(f.readline() + "boş" == "boş"):
                    turnCounter = 0
                
            try:
            #check if the space is available
                if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, moon)
                    break
        
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occurred. Please try again")
                
        winner = checkWinner(moon)
        turnCounter += 1         
        
    else:
        printGameBoard()
        print("\n", players.get(sun), " plays")
        
        while True:
            
            pickedSpace = input("\n Choose a space or press Q: ")
            

            if pickedSpace != "Q" :
                sun_array.append(pickedSpace)
                
                coordinate = coordinateParser(pickedSpace)
                
                f = open("tahta.txt","r+")
                h = open("hamle.txt","r+")
                
                tahta = pickedSpace
                f.write(tahta)

                h.write(sun_array[turnCounter % 2 - 1])
  
            else:
                print("Game stopped")
                print("Welcome to Connect 4 Game: ")
                print("----------------------------")
                x = input("Please enter NEW GAME or CONTINUE: ")
                
                f = open("tahta.txt","r+")
                h = open("hamle.txt", "r+")
                
                menu(x,f,h)
                f = open("tahta.txt","r")
                if(f.readline() + "boş" == "boş"):
                    turnCounter = 0

                break
                
                
            try:
            #check if the space is available
                if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, sun)
                    break
        
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occurred. Please try again")
            
        winner = checkWinner(sun)
        turnCounter += 1  
            
    if(winner):
        printGameBoard()
        
        f.close()
        h.close()
        
        os.remove("tahta.txt")
        os.remove("hamle.txt")
        break
  
   
