import os, sys, random

money=0
items=[]
currentLoc=["5","8"]
availableItems=["flashlight", "crowbar"]
file="user.txt"


#Function for saving inventory and money
def save(inventory, money):
  	#If file does not exist create one
  	if not os.path.isfile(file):
      file_open=open("user.txt", "a")
    file_open=open(file, "a")
	#Write inventory to file
	file_open.write("Inventory: " + ",".join(inventory) + "\n")
    #Write money to file
    file_open.write("money: " + str(money) + "\n")
    file_open.close()
    
def open_file():
  file_open = open(file, "r") 
  read_file = file_open.read()
  
  
  
def shop(money):
  print("You have %i money(s)" % money + "\n")
  print("There are 5 available items you can purchase, \n Item #(1) Flashlight \n #(2) Crowbar \n #(3)")
  newItem = input("Which one would you like to purchase?: ")
  #If item is already in inventory
  if newItem in items:
    print("You already have that.")
    return None
  x=0
  #While length is less than the array
  while x <= len(availableItems):
    #If x is equal to the item the user entered
    if x == int(newItem):
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

while True:
  print("To visit the shop type \"shop\",\n for your inventory type \"inventory\",\n to make a move type \"move\", to save type \"save\"\n")
  user_input = input("\n Action: ")
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
