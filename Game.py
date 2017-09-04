import os, sys, random

money=0
items=[]
availableItems=["flashlight", "crowbar"]

def shop(money):
  print("You have %i money(s)" % money + "\n")
  print("There are 5 available items you can purchase, \n Item #(1) Flashlight \n #(2) Crowbar \n #(3)")
  newItem = input("Which one would you like to purchase?: ")
  x=0
  #While length is less than the array
  while x <= len(availableItems):
    if x == int(newItem):
      items.append(availableItems[x-1])
    else:
      x=x+1
  #When User buys a new item
  inventory(items)
  
#For user inventory
def inventory(items):
  itemsString=",".join(items)
  print("\n You have: %s" % itemsString + "\n")
  
while True:
  user_input=input("To visit the shop type \"shop\",\n for your inventory type \"inventory\",\n for all other options follow later directions: ")
  if user_input == "shop":
    shop(money)
  elif user_input == "inventory":
    inventory(items)
