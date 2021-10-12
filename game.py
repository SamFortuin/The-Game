#99059050, Sam Fortuin
import time, os, sys, simple_colors

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
You can't find your dog in it's usual spot.\n\
Where will you look for your dog?\n\
·The Kitchen\n·The Living Room\n·The Bedroom\n")

#input question is in the print_slow above.
room1= input("")
room1 = room1.lower().replace(" ","").replace("the","")
#clear screen and little bit of text before next question
clearScreen(0.2)
print_slow("As you walk towards the ")
print_slow(room1)
print_slow(" you wonder what the dog could be doing")
clearScreen(0.2)

if room1 == "kitchen":
  print_slow("You see your meds, a knife, and your favorite spoon.\nWhich one do you pick up?\n")
  item = input("")
  if item == "meds":
    meds = input("Do you take your meds or leave them?")
  elif item == "knife":
    knife = input("was")
  elif "spoon" in item:
    spoon = input("wa")
elif room1 == "livingroom":
  exit()
elif room1 == "bedroom":
  exit()
else:
  exit()