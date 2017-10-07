import os, sys
from random import *
money=0
items=[]
#starting pos
currentLoc=[0,0]

#For moving x distance
getLoc=0
#set game boundaries
min_boundaries=[0,0]
max_boundaries=[2,2]

#Generate the treasure/and other treasure related variables
treasurex=randint(1,2)
treasurey=randint(1,2)
treasureLoc=[treasurex,treasurey]
print("Hint: ",treasureLoc)
#Where the random money prize will be generated
max_earnings=150
generate_money=randint(1,max_earnings)

availableItems=["flashlight", "crowbar", "sword", "pistol"]
availableItemPrices=["30", "50", "65", "250"]
file="user.txt"

#Function for saving inventory and money
def save(inventory):
        #If file does not exist create one
        if not os.path.isfile(file):
                file_open=open(file, "a")
        #Write inventory to file
        file_open.write("Inventory: " + ",".join(inventory) + "\n")
        #Write money to file
        file_open.write("money: " + str(money) + "\n")
        file_open.close()

def open_file():
  if not os.path.isfile(file):
    file_open(file, "a")

  with open(file, 'r') as f:
        for line in f:
          if "money: " in line:
            money=line.split("money: ", 1)
            money=int(money[1])
            print("money: ", money)
#Check if there is enough money
def isEnough(price):
    if price <= money:
        #Allow changing of global varaible money
        global money
        money=money-price
        return True
    else:
        return False
def shop():
  print("You have %i dollars" % money + "\n")
  #Split array into readable text
  splitAvailableItems=""
  for numVar in range(0, len(availableItems)):
        splitAvailableItems+="#%i) "%(numVar+1)+availableItems[numVar] + "\n"
  print("There are %i available items you can purchase, Item \n%s"%(len(availableItems), splitAvailableItems))
  newItem = raw_input("Which one would you like to purchase?: ")
  #If item is already in inventory
  x=0
  #While length is less than the array
  for x in range(0, len(availableItems)):
    #If x is equal to the item the user entered
    if x == int(newItem):
        if availableItems[x-1] in items:
                print("You already have that.")
                return None
                break
        if isEnough(availableItemPrices[x-1]):
            items.append(availableItems[x-1])
        else:
            print("Not enough money")
        #Exit loop
        break
#For user inventory
def inventory(items):
  itemsString=",".join(items)
  print("\n You have: %s" % itemsString + "\n")


def prize():
    print("You have won: %i " % generate_money + "dollars")
    return generate_money

#For moves
def move():
  #currentLocString=",".join(currentLoc)
  print("You are currently ", currentLoc)
  print("You can move (right),(left),(up),(down)")
  newmove=raw_input("move: ")
  if newmove.lower() == "right":
    #Get last value of array
    getLoc=currentLoc[-1]
    getLoc=getLoc+1
    if(getLoc>max_boundaries[-1]):
          print("Sorry, you've hit a boundary")
          return None
    #Sets new x location to array
    currentLoc[-1]=getLoc
    #print("You are now here: %d" % int(getLoc))
    print(currentLoc)

  elif(newmove.lower() == "down"):
      getLoc=currentLoc[0]
      getLoc=getLoc+1
      if(getLoc<min_boundaries[0]) or (getLoc>max_boundaries[0]):
          print("Sorry, you've hit a boundary")
          return None
      currentLoc[0]=getLoc
      #print("You are now here: %d" % int(getLoc))
      print(currentLoc)

  elif(newmove.lower() == "up"):
    getLoc=currentLoc[0]
    getLoc=getLoc-1
    if(getLoc<min_boundaries[0]):
        print("Sorry, you've hit a boundary")
        return None
    currentLoc[0]=getLoc
    print(currentLoc)

  elif(newmove.lower() == "left"):
      getLoc=currentLoc[-1]
      getLoc=getLoc-1
      if(getLoc<min_boundaries[0]):
           print("Sorry, you've hit a boundary")
           return None

      currentLoc[-1]=getLoc
      print(currentLoc)
      return currentLoc

  else:
      print("Unknown option")
      return None
