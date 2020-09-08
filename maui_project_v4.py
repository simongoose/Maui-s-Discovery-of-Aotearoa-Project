# maui_project_v4.py
# Created by: Simon Lee
# Created on: 18/08/2020
"""
Version 4

"""
# create variables, lists, import modules etc.
import random
game = 'y'
DIFFICULTIES = {7 : "Easy", 5 : "Medium", 3 : "Hard", 1 : "Impossible"}
SEA_STATEMENTS = [
"You sail to the next location, but all you see is the open sea.",
"A chilling wind whooshes past as you see nothing but water around you.",
"The great ocean is all you can see as you sail along.",
"There is no land or fish nearby, the deep blue sea surrounds you.",
"Your boat is the only sign of life in the vast ocean.",
"You sail further, but all you see is the ocean. Determined, you press on to find Aotearoa.",
"Sail lifted, you voyage further into open water, with nothing else to see.",
"Your eyes can only see the ocean, and how far it strectches.",
"Waves strectch out before your waka. Nothing but sea surrounds you."]

# get starting locations of fish, player and land
def grid():
    taken_locs = []
    # starting location
    pos_x = random.randint(1,5)
    pos_y = random.randint(1,5)
    taken_locs.append([pos_x, pos_y])

    # land location
    land_x = random.randint(1,5)
    land_y = random.randint(1,5)
    while [land_x, land_y] in taken_locs:
        land_x = random.randint(1,5)
        land_y = random.randint(1,5)
    taken_locs.append([land_x, land_y])

    # fish locations
    fish_locs = []
    for i in range(0,3):
        fish_x = random.randint(1,5)
        fish_y = random.randint(1,5)
        while [fish_x, fish_y] in taken_locs:
            fish_x = random.randint(1,5)
            fish_y = random.randint(1,5)
        taken_locs.append([fish_x, fish_y])
        fish_locs.append([fish_x, fish_y])

    # return locations
    return [pos_x, pos_y], [land_x, land_y], fish_locs


# movement function: processes user input and moves player
def move(position):
    moves = ['u', 'd', 'l', 'r']
    print("You are currently in location {}.".format(position))
    # ask for direction and check that the move is valid
    direction = input("""Would you like to move:
(U) - Up
(D) - Down
(L) - Left
(R) - Right
Enter direction: """).lower()
    while direction not in moves:
        print("Please enter a valid move.")
        direction = input("Enter direction: ").lower()

    # move the player in the direction
    if direction == 'u':
        if position[1] >= 5:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[1] += 1
            return 'y'

    elif direction == 'd':
        if position[1] <= 1:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[1] -= 1
            return 'y'

    elif direction == 'l':
        if position[0] <= 1:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[0] -= 1
            return 'y'

    elif direction == 'r':
        if position[0] >= 5:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[0] += 1
            return 'y'


# life function: counts how many lives/fish the player has and how many moves they have done
def life(moved, moves, lives):

    if moved == 'y':
        moves += 1
        
        # if the player has moved twice, take away one fish
        if moves % 2 == 0 and moves != 0:
            lives -= 1
            print(moves, lives, moved)
        
            if lives > 0:
                print("""\n*****ATTENTION VOYAGER!*****
Your men have eaten 1 container of fish after 2 days!""")
                print("You now have {} containers left!".format(lives))
            
            elif lives <= 0:
                print("""\n*****ATTENTION VOYAGER!*****
Unfortunately, you and your men have eaten all the fish!
You have no choice but to return to your homeland and search for Aotearoa another day!""")
            
    elif moved == 'n':
        pass

    return moves, lives

# interact function: lets user fish fish and land on the land
def interact(position, land, fish, lives):
    found = 'n'
    # if they found land, end the round and let them know they won
    if position == land:
        print("""\n*****ATTENTION VOYAGER*****
You spot a long white cloud streaking through the lonely sky!
Enchanted, you decide to sail towards it...
At last, you have discovered the pristine shores of Aotearoa!
------------------+
       \          |
        \         |
        \\         |
         \\\       |
          ) `-')  |
         <_ o /   |
           \  /   |    
           / /    |    
      /_,, ~~     |
     /   )        |
     |  /         |     
    /  _>         |       
   /  /           |       
  /   |           |
 |    /           |
 \___/            |          
   o""")
        found = 'y'

    # if they found fish, let them know and add one to 'lives'
    elif position in fish:
        lives += 1
        print("""\n*****ATTENTION VOYAGER!*****
Your fishermen call you over to a commotion on the side of your waka!
Your fishermen have caught a really massive school of fish!""")
        print("You now have 1 more container of fish, so you have a total of {}!".format(lives))
        fish.remove(position)
        found = 'n'

    elif lives > 0:
        print("\n{}\n".format(SEA_STATEMENTS[random.randint(0,8)]))

    return found, lives


# difficulty function: lets user pick the difficulty (amount of lives to start with)
def difficulty(lives):
    options = ['a', 'b', 'c', 'd']
    print("The current difficulty is {}.".format(DIFFICULTIES[lives]))
    difficulty = input("""\nWhat difficulty would you like to play on?

A) Easy (Start with 7 containers of fish)
B) Medium (Start with 5 containers of fish)
C) Hard (Start with 3 containers of fish)
D) Impossible (Start with 1 container of fish)

Select a difficulty: """).lower().strip()

    while difficulty not in options:
        print("\nPlease enter a valid option.")
        print("The current difficulty is {}.".format(DIFFICULTIES[lives]))
        difficulty = input("""\nWhat difficulty would you like to play on?

A) Easy (Start with 7 containers of fish)
B) Medium (Start with 5 containers of fish)
C) Hard (Start with 3 containers of fish)
D) Impossible (Start with 1 container of fish)

Select a difficulty: """).lower().strip()

    if difficulty == 'a':
        lives = 7

    elif difficulty == 'b':
        lives = 5

    elif difficulty == 'c':
        lives = 3

    elif difficulty == 'd':
        lives = 1
    return lives


# main function: the main menu
def main(lives):
    options = ['a', 'b', 'c', 'd']
    option = 'n'
    
    while option not in options:
        option = input("""\n
--------------------
A) Play A Game
B) How To Play
C) Select Difficulty
D) Quit The Game
--------------------

Select an option: """).lower().strip()
        if option not in options:
            print("Please choose a valid option from the list.\n")

    if option == 'a':
        moves = 0
        position, land, fish = grid() 
        print(land)
        print(position)
        while lives > 0:
            moved = move(position)
            moves, lives = life(moved, moves, lives)
            print(lives)
            win, lives = interact(position, land, fish, lives)
            if win == 'y': 
                print("Congratulations, you completed the game in {} moves!".format(moves))
                print("\n\n\n\n\n\n\n-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                return 'W', lives
            else:
                pass
        return 'N', lives
                

    elif option == 'b':
        print("""\nWelcome Voyager, to Maui's Discovery.
The goal of the game is simple, FIND AOTEAROA. You are
spawned in on a 5x5 grid of unexplored sea.

    1     2     3     4     5
 +-----+-----+-----+-----+-----+
 |     |     |     |     |     |
1|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
2|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
3|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
4|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
5|     |     |     |     |     |
 |     |     |     |     |     |
 +-----+-----+-----+-----+-----+

---------------------------------------------------------------------------

On your mighty waka, you can move in 4 directions, Up, Down, Left and Right.

You start with a number of containers of fish, depending on your difficulty,
which you can select in the menu.

But be careful! Every two moves you and your men will eat one
container of fish! There are 3 other spots where schools of fish can
be hooked up by your men, providing you with further food.

---------------------------------------------------------------------------

       /`·.¸
     /¸...¸`:·                                              
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´ 

If you run out of fish, you will be forced to return to your
homeland, and search for Aotearoa another day...

---------------------------------------------------------------------------

Good luck voyager, I hope you find the legendary land of Aotearoa!
""")
        return 'N', lives

    elif option == 'c':
        lives = difficulty(lives)
        return 'N', lives

    elif option == 'd':
        print("Thank you for playing the game!")
        return 'Q', lives

while game == 'y':
    print("""                        _ _           _ _                                   
                       (_| )         | (_)                                  
  _ __ ___   __ _ _   _ _|/ ___    __| |_ ___  ___ _____   _____ _ __ _   _ 
 | '_ ` _ \ / _` | | | | | / __|  / _` | / __|/ __/ _ \ \ / / _ \ '__| | | |
 | | | | | | (_| | |_| | | \__ \ | (_| | \__ \ (_| (_) \ V /  __/ |  | |_| |
 |_| |_| |_|\__,_|\__,_|_| |___/  \__,_|_|___/\___\___/ \_/ \___|_|   \__, |
                                                                       __/ |
                                                                      |___/""")
    while True == True:
        lives = 7
        again, lives = main(lives)
        if again == "N":
            pass
        elif again == 'Q':
            game = 'n'
            break
        elif again == 'W':
            break
