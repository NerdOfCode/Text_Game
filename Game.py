import os, sys, random

money=0
items=[]
currentLoc=["0","0"]
availableItems=["flashlight", "crowbar", "sword"]
file="user.txt"


#Function for saving inventory and money
def save(inventory, money):
        #If file does not exist create one
        if not os.path.isfile(file):
                file_open=open(file, "a")
        #Write inventory to file
        file_open.write("Inventory: " + ",".join(inventory) + "\n")
        #Write money to file
        file_open.write("money: " + str(money) + "\n")
        file_open.close()
    
def open_file():
  #Make money available everywhere
  global money
  if not os.path.isfile(file):
    file_open(file, "a")

  with open(file, 'r') as f:
        for line in f:
          if "money: " in line:
            money=line.split("money: ", 1)
            money=int(money[1])
            print("money: ", money)
def shop(money):
  print("You have %i money(s)" % money + "\n")
  #Split array into readable text
  splitAvailableItems=""
  for numVar in range(0, len(availableItems)):
        splitAvailableItems+="#%i) "%(numVar+1)+availableItems[numVar] + "\n"
  print("There are %i available items you can purchase, Item \n%s"%(len(availableItems), splitAvailableItems))
  newItem = input("Which one would you like to purchase?: ")
  #If item is already in inventory
  x=0
  #While length is less than the array
  while x <= len(availableItems):
    #If x is equal to the item the user entered
    if x == int(newItem):
        if availableItems[x-1] in items:
                print("You already have that.")
                return None
                break
        items.append(availableItems[x-1])
        #Exit loop
        break
    else:
      x=x+1
#For user inventory
def inventory(items):
  itemsString=",".join(items)
  print("\n You have: %s" % itemsString + "\n")
  
#For moves
def move(newMove):
        currentLocString=",".join(currentLoc)
        print("You are currently %s"% currentLocString)
        newmove=raw_input("Enter ")
  
  
  
  
while True:
  print("To visit the shop type \"shop\",\n for your inventory type \"inventory\",\n to make a move type \"move\", to save type \"save\"\n")
  user_input = raw_input("\n Action: ")
  if user_input.lower() == "shop":
    shop(money)
  elif user_input.lower() == "inventory":
    inventory(items)
  elif user_input.lower() == "move":
    newMove=input("Enter your move: ")
    move(newMove)
  elif user_input.lower() == "exit":
    sys.exit(0)
  elif user_input.lower() == "save":
    save(items, money)
  elif user_input.lower() == "open":
    open_file()
  else:
    print("You appear to have made a typo, please try again")
