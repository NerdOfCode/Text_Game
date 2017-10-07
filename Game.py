import os, sys, random

money=0
items=[]
#starting pos
currentLoc=[0,0]

#For moving x distance
getLoc=0
#set game boundaries
min_boundaries=[0,0]
max_boundaries=[2,2]



availableItems=["flashlight", "crowbar"]
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
    if(getLoc<max_boundaries[0]):
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

  else:
      print("Unknown option")
      return None

  
while True:
  print("To visit the shop type \"shop\",\n for your inventory type \"inventory\",\n to make a move type \"move\", to save type \"save\"\n")
  user_input = raw_input("\n Action: ")
  if user_input.lower() == "shop":
    shop(money)
  elif user_input.lower() == "inventory":
    inventory(items)
  elif user_input.lower() == "move":
    move()
  elif user_input.lower() == "exit":
    sys.exit(0)
  elif user_input.lower() == "save":
    save(items, money)
  elif user_input.lower() == "open":
    open_file()
  else:
    print("You appear to have made a typo, please try again")
