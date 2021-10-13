#99059050, Sam Fortuin
import time, os, sys

#print slow from sabastion on stackoverflow, good lad
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

#clears screen after given time
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def invalidInput():
  print("\ninvalid input, exeting program")
  time.sleep(0.2)
  exit()

def listPrint(roomList, roomCount):
  roomCount = len(roomList)
  for i in range(roomCount):
    time.sleep(0.08)
    print(roomList[i])

#title screen
print(" \
                                                              _____^_       \n  \
                                                            |    |  \       \n  \
                                                            \   /  ^ |      \n  \
                                                           / \_/   0  \     \n  \
                                                          /            \    \n  \
                                                         /    ____      0   \n  \
                                                        /      /  \___ _/   \n  \
             __                __        __    __                      __                          __                       __      \n  \
           /\ \              /\ \__    /\ \__/\ \                    /\ \                        /\ \          __         /\ \      \n  \
 __  __  __\ \ \___      __  \ \ ,_\   \ \ ,_\ \ \___      __        \_\ \    ___      __        \_\ \    ___ /\_\    ___ \ \/      \n  \
/\ \/\ \/\ |\ \  _ `\  /'__`\ \ \ \/    \ \ \/\ \  _ `\  /'__`\      /'_` \  / __`\  /'_ `\      /'_` \  / __`\/\ \ /' _ `\|/       \n  \
\ \ \_/ \_/| \ \ \ \/\ \L\.\_\ \ \_      \ \ \_\ \ \ \ \/\  __/     /\ \L\ \/\ \L\ \/\ \L\ \    /\ \L\ \/\ \L\ \ \ \/\ \/\ \        \n  \
 \ \___x___/  \ \_\ \_\ \__/.\_|\ \__\    \ \__\| \_\ \_\ \____\    \ \___,_\ \____/\ \____ \   \ \___,_\ \____/\ \_\ \_\ \_\       \n  \
  \/__//__/    \/_/\/_/\/__/\/_/ \/__/     \/__/ \/_/\/_/\/____/     \/__,_ /\/___/  \/___L\ \   \/__,_ /\/___/  \/_/\/_/\/_/       \n  \
                                                                                       /\____/                                      \n  \
                                                                                       \_/__/                                       \n  \
                            ┌─┐  ┌┬┐┌─┐┌─┐  ┌─┐┬┌┐┌┌┬┐┬┌┐┌┌─┐  ┌─┐┌┬┐┬  ┬┌─┐┌┐┌┌┬┐┬ ┬┬─┐┌─┐     \n  \
                            ├─┤   │││ ││ ┬  ├┤ ││││ │││││││ ┬  ├─┤ ││└┐┌┘├┤ │││ │ │ │├┬┘├┤      \n  \
                            ┴ ┴  ─┴┘└─┘└─┘  └  ┴┘└┘─┴┘┴┘└┘└─┘  ┴ ┴─┴┘ └┘ └─┘┘└┘ ┴ └─┘┴└─└─┘     \n  \
")
clearScreen(0.5)

#ask which room player wants to go to
print_slow("You return home after a long day of work.\n\
As you enter the living room you can't find your dog in it's usual spot.\n\
Where will you look for your dog?\n\
·The Kitchen\n·The Bathroom\n·The Bedroom\n")

#input question is in the print_slow above.
room= input("")
#cleanup for the if statement
room = room.lower().replace("the","").replace(" ","")
#clear screen and little bit of text before next question
clearScreen(0.2)
print_slow("You walk towards the ")
print_slow(room)
clearScreen(0.5)

#lists for the 3 items player needs to pick up
invList = ["item0","item1","item2"]
kitchenList = ["·your meds", "·a knife", "·a spoon"]
bathList = ["·", "·", "·"]
bedList = ["·", "·", "·"]

#var placeholders for listPrint
kitchenCount = 0
bathCount = 0
bedCount = 0

#meds var for reasons
medsTaken = False

def roomsItems(itemNum): 
  #if statement for rooms and items
  if room == "kitchen":
    print_slow("You see some items laying in the kitchen:\n")
    listPrint(kitchenList,kitchenCount)
    print_slow("Which one do you pick up?\n")
    item = input("")
    item = item.replace(" ","").replace("the","").replace("a","").replace("your","")
    if item == "meds":
      print_slow("You pick up your meds\n")
      invList[itemNum] = "meds"
      #removes item from the kitchen
      del kitchenList[0]
      print_slow("Do you want to take your meds?\n")
      medsTakenInput = input("")
      medsTakenInput = medsTakenInput.lower()
      if medsTakenInput == "y" or medsTakenInput == "yes":
        medsTaken = True
        #sets item slot 0 back to clean because player consumed the meds
        item[itemNum] = "item0"
      else:
        medsTaken = False
    elif item == "knife":
      print_slow("You pick up the knife")
      invList[itemNum] = "knife"
      #removes the item from the kitchen
      del kitchenList[1]
    elif item == "spoon":
      print_slow("You pick up the spoon")
      invList[itemNum] = "spoon"
      #removes the item from the kitchen
      del kitchenList[2]
    else:
      invalidInput()

  elif room == "bathroom":
    print_slow("As you enter the living room you see:")
    listPrint(bathList,bathCount)

  elif room == "bedroom":
    exit()

  else:
    exit()

for i in range(3):
  roomsItems(i)