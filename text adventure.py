    

    
# some rooms

# treasure room
def treasure_room():
  # some prompts
  print("\nYou are now in a room filled with treasure!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). You find a sapphire necklace, and decide to wear it.")
  print("2). You take a handful of silver and go through the door.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("The necklace was cursed! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you survived! Congrats you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
   game_over("Go and learn how to type a number.")


# viking room
def viking_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThere is a tall viking here, who is a fearsome warrior.")
  print("Behind the viking is another door.")
  print("The viking is wiping some fresh blood from his sword.")
  print("What would you do? (1 or 2)")
  print("1). Taunt the viking, as you wield a sword.")
  print("2). You attempt to speak danish, telling the viking his boat has burst into flames.")

  # take input()
  answer = input(">")
   
  if answer == "1":
    # the player is dead!
    game_over("The viking strikes a blow to your head with his shield. You die!")
  elif answer == "2":
    # lead him the treasure()
    print("""\nYour attempt was successful, the viking rushes out the room in panic. 
    You can go through it now!""")
    treasure_room()
  else:
    # else call game_over() function with the "reason" argument
   viking_room()


# monster room
def wolf_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of a hungry wolf!")
  print("The wolf is sleeping.\nBehind the wolf, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Throw a rock at the wolf to create a momentary distraction")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead player to the treasure()
    treasure_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The wolf knocks you to the ground and eats you.")
  else:
    # game_over() with "reason"
    wolf_room()


# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()


def start():
  # give some prompts.
  print("\nYou are standing in a small dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to viking_room()
    viking_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to wolf_room()
    wolf_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()