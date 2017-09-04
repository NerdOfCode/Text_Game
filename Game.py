import os, sys, random

money=0
items=[]

def shop(money):
  print("You have %i money(s)" % money + "\n")
  print("There are 5 available items you can purchase, \n Item #(1) Flashlight \n #(2) Crowbar \n #(3)")
  newItem = input("Which one would you like to purchase?: ")
  
  items.append(newItem)
  #When User buys a new item
  inventory(items)
  
def inventory(items):
  itemsString=",".join(items)
  print("You have: %s" % itemsString)
  
while True:
  user_input=input("To visit the shop type \"shop\", for your inventory type \"inventory\", for all other options follow later directions ")
  
