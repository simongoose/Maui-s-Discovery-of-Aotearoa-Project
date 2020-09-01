# maui_project_v3.py
# Created by: Simon Lee
# Created on: 18/08/2020
"""
Version 3

"""
# create variables, lists, import modules etc.
import random
difficulties = {7 : "Easy", 5 : "Medium", 3 : "Hard", 1 : "Impossible"}


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
    print("\nYou are currently in location {}.".format(position))
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
    found = 'y'
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

    return found, lives


# difficulty function: lets user pick the difficulty (amount of lives to start with)
def difficulty(lives):
    options = ['a', 'b', 'c', 'd']
    print("The current difficulty is {}.".format(difficulties[lives]))
    difficulty = input("""\nWhat difficulty would you like to play on?

A) Easy (Start with 7 containers of fish)
B) Medium (Start with 5 containers of fish)
C) Hard (Start with 3 containers of fish)
D) Impossible (Start with 1 container of fish)

Select a difficulty: """).lower().strip()

    while difficulty not in options:
        print("\nPlease enter a valid option.")
        print("The current difficulty is {}.".format(difficulties[lives]))
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
def main():
    options = ['a', 'b', 'c', 'd']
    lives = 7

    # ask user what they want to do in the program
    print("WELCOME TO MAUI'S DISCOVERY: THE GAME")
    option = input("""\n--------------------
A) Play A Game
B) How To Play
C) Select Difficulty
D) Quit The Game
--------------------
Select an option: """).lower().strip()
    
    while option not in options:
        print("\nPlease enter a valid option.")
        option = input("""\n--------------------
A) Play A Game
B) How To Play
C) Select Difficulty
D) Quit The Game
--------------------
Select an option:""").lower().strip()

    if option == 'a':
        moves = 0
        position, land, fish = grid() 
        print(land)
        print(position)
        while lives >= 0: 
            moved = move(position) 
            moves, lives = life(moved, moves, lives) 
            win, lives = interact(position, land, fish, lives) 
        if win == 'win': 
            print("Congratulations, you completed the game in {} moves!".format(moves)) 
        else: 
            pass
        return 'N'

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

          XXXXXXXXX
     XXXXX         XXXXXXXX             X
  XXX                      XXXXXX     XX X
 X     XX                        X   X    X
X      XXX                        X X     X
X                                  X      X
X                                 X X     X
 X                               X   X    X
  XXX                      XXXXXX     XX X
     XXXXX         XXXXXXXX             X
          XXXXXXXXX


If you run out of fish, you will be forced to return to your
homeland, and search for Aotearoa another day...

---------------------------------------------------------------------------

Good luck voyager, I hope you find the legendary land of Aotearoa!
""")
        return 'N'

    elif option == 'c':
        lives = difficulty(lives)
        return 'N'

    elif option == 'd':
        print("Thank you for playing the game!")
        return 'Q'

while True == True:
    again = main()
    if again == 'N':
        pass
    elif again == 'Q':
        break
