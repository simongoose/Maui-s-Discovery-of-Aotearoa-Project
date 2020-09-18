# maui_project_v6.py
# Created by: Simon Lee
# Created on: 18/08/2020
"""
Version 6

"""
# create variables, lists, import modules etc.
import random
toggle = 2
game = 'y'
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
DIVIDER = "--------------------"
TITLE = """                        _ _           _ _                                   
                       (_| )         | (_)                                  
  _ __ ___   __ _ _   _ _|/ ___    __| |_ ___  ___ _____   _____ _ __ _   _ 
 | '_ ` _ \ / _` | | | | | / __|  / _` | / __|/ __/ _ \ \ / / _ \ '__| | | |
 | | | | | | (_| | |_| | | \__ \ | (_| | \__ \ (_| (_) \ V /  __/ |  | |_| |
 |_| |_| |_|\__,_|\__,_|_| |___/  \__,_|_|___/\___\___/ \_/ \___|_|   \__, |
                                                                       __/ |
                                                                      |___/"""

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


# possible_moves function: calculates which moves are possible and returns them so that they can be printed to the user
def possible_moves(position, toggle):
    print(toggle)
    passover = []
    if position[1] == 5:
        passover.append('u')
    if position[1] == 1:
        passover.append('d')
    if position[0] == 5:
        passover.append('r')
    if position[0] == 1:
        passover.append('l')

    if toggle == 2:
        u = "- Move to {}".format([position[0], position[1] + 1])
        d = "- Move to {}".format([position[0], position[1] - 1])
        l = "- Move to {}".format([position[0] - 1, position[1]])
        r = "- Move to {}".format([position[0] + 1, position[1]])
    elif toggle == 1:
        u = ""
        d = ""
        l = ""
        r = ""
    
    if 'u' in passover:
        u = "- Can't Move Up"
    if 'd' in passover:
        d = "- Can't Move Down"
    if 'l' in passover:
        l = "- Can't Move Left"
    if 'r' in passover:
        r = "- Can't Move Right"

    return u, d, l, r
        

# movement function: processes user input and moves player
def move(position, moves, toggle):
    MOVES = ['1', '2', '3', '4']
    if moves == 0:
        print("\nThis is the first day of your voyage.")
    else:
        print("\nThis is Day {} of your voyage.".format(moves))
    print("You are currently in location {}.".format(position))
    u, d, l, r = possible_moves(position, toggle)
    
    # ask for direction and check that the move is valid
    direction = input("""Would you like to move:
(1) Up {}
(2) Down {}
(3) Left {}
(4) Right {}
Enter direction: """.format(u, d, l, r)).lower()
    while direction not in MOVES:
        print("Please enter a valid move.")
        direction = input("Enter direction: ").lower()

    # move the player in the direction
    if direction == '1':
        if position[1] >= 5:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[1] += 1
            return 'y'

    elif direction == '2':
        if position[1] <= 1:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[1] -= 1
            return 'y'

    elif direction == '3':
        if position[0] <= 1:
            print("Sorry, you can't go off the edge. Enter another direction.")
            return 'n'
        else:
            position[0] -= 1
            return 'y'

    elif direction == '4':
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
                print("You voyaged for a total of {} days, but you did not find land.".format(moves))
                print("Better luck next voyage! =)")
                print("\n\n\n{}".format(TITLE))
            
    elif moved == 'n':
        pass

    return moves, lives

# interact function: lets user fish fish and land on the land
def interact(position, land, fish, lives, moved):
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
        print(DIVIDER)
        found = 'y'

    # if they found fish, let them know and add one to 'lives'
    elif position in fish:
        lives += 1
        print("""\n*****ATTENTION VOYAGER!*****
Your fishermen call you over to a commotion on the side of your waka!
Your fishermen have caught a really massive school of fish!""")
        print("You now have 1 more container of fish, so you have a total of {}!".format(lives))
        print(DIVIDER)
        fish.remove(position)
        found = 'n'

    elif lives > 0 and moved == 'y':
        print("\n{}\n".format(SEA_STATEMENTS[random.randint(0,8)]))
        print(DIVIDER)

    return found, lives


# difficulty function: lets user pick the difficulty (amount of lives to start with)
def difficulty(lives):
    lives = 7
    OPTIONS = ['1', '2', '3', '4']
    difficulty = input("""------------------------------------------
What difficulty would you like to play on?

(1) Easy            [7 containers of fish]
(2) Medium          [5 containers of fish]
(3) Hard            [3 containers of fish]
(4) Impossible       [1 container of fish]

Select a difficulty: """).lower().strip()

    while difficulty not in OPTIONS:
        print("\nPlease enter a valid option.")
        difficulty = input("""\nWhat difficulty would you like to play on?

A) Easy (Start with 7 containers of fish)
B) Medium (Start with 5 containers of fish)
C) Hard (Start with 3 containers of fish)
D) Impossible (Start with 1 container of fish)

Select a difficulty: """).lower().strip()

    if difficulty == '1':
        lives = 7
        print("The difficulty has been changed to easy.")

    elif difficulty == '2':
        lives = 5
        print("The difficulty has been changed to medium.")

    elif difficulty == '3':
        lives = 3
        print("The difficulty has been changed to hard.")

    elif difficulty == '4':
        lives = 1
        print("The difficulty has been changed to impossible.")
    return lives


# main function: the main menu
def main(lives, toggle):
    OPTIONS = ['1', '2', '3', '4', '5']
    option = 'n'
    
    while option not in OPTIONS:
        option = input("""\n
--------------------
(1) Play A Game
(2) How To Play
(3) Select Difficulty
(4) Settings
(5) Quit The Game
--------------------

Select an option: """).lower().strip()
        if option not in OPTIONS:
            print("Please choose a valid option from the list.\n")

    if option == '1':
        moves = 0
        position, land, fish = grid()
        while lives > 0:
            moved = move(position, moves, toggle)
            moves, lives = life(moved, moves, lives)
            win, lives = interact(position, land, fish, lives, moved)
            if win == 'y': 
                print("Congratulations, you found Aotearoa after {} days of voyaging!".format(moves))
                print("\n\n\n\n\n\n\n--------------------------------------------------------------")
                return 'W', lives, toggle
            else:
                pass
        return 'N', lives, toggle
                

    elif option == '2':
        print("""\nWelcome Voyager, to Maui's Discovery.
The goal of the game is simple, FIND AOTEAROA. You are
spawned in on a 5x5 grid of unexplored sea.


 +-----+-----+-----+-----+-----+
 |     |     |     |     |     |
5|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
4|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
3|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
2|     |     |     |     |     |
 |     |     |     |     |     |
 +-----------------------------+
 |     |     |     |     |     |
1|     |  x  |     |     |     |
 |     |     |     |     |     |
 +-----+-----+-----+-----+-----+
    1     2     3     4     5

(Note: The x on the grid is in spot [2,1])

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
        return 'N', lives, toggle

    elif option == '3':
        lives = difficulty(lives)
        return 'N', lives, toggle

    elif option == '4':
        print("""\n{}\nWould you rather have the game look like:
(1) Up
(2) Up - Move to [3, 4]
{}""".format(DIVIDER, DIVIDER))
        toggle = input("Which one would you like? (1 or 2) ")
        while toggle != '1' and toggle != '2':
            print("Please enter 1 or 2.")
            toggle = input("Which one would you like? (1 or 2) ")
        print(toggle)
        return 'N', lives, toggle

    elif option == '5':
        print("Thank you for playing the game!")
        return 'Q', lives, toggle

while game == 'y':
    lives = 7
    print(TITLE)
    while True == True:
        again, lives, toggle = main(lives, toggle)
        if again == "N":
            pass
        elif again == 'Q':
            game = 'n'
            break
        elif again == 'W':
            break
