import time, os, sys

list = [1, 2, 2.3, 78, "james"]
listCount = 0
invList = [1,2,3,4,5]

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

def listPrint(roomList, roomCount):
  roomCount = len(roomList)
  for i in range(roomCount):
    time.sleep(0.08)
    print(roomList[i])

def itemPickup(item,listItem,pickupNum):
  print_slow("You pick up the ")
  print_slow(item)
  invList[pickupNum] = item
  #removes the item from the kitchen
  del listItem

listPrint(invList,listCount)
itemPickup("Towel",invList[2],3)
listPrint(invList,listCount)