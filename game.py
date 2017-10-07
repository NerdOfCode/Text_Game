from func import *

while True:
  print("To visit the shop type \"shop\",\n for your inventory type \"inventory\",\n to make a move type \"move\", to save type \"save\"\n")
  user_input = raw_input("\n Action: ")
  if user_input.lower() == "shop":
    shop()
  elif user_input.lower() == "inventory":
    inventory(items)
  elif user_input.lower() == "move":
    move()
    if currentLoc == treasureLoc:
        prize()
        money=generate_money
  elif user_input.lower() == "exit":
    sys.exit(0)
  elif user_input.lower() == "save":
    save(items, money)
  elif user_input.lower() == "open":
    open_file()
  else:
    print("You appear to have made a typo, please try again")
