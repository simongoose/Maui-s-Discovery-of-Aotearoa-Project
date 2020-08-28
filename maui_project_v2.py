# maui_project_v2.py
# Created by: Simon Lee
# Created on: 18/08/2020
"""
Version 2

"""
# create variables, lists, import modules etc.
import random
moves = 0
lives = 3


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
def move():
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

    return found

      
position, land, fish = grid()
print(land)
while lives >= 0:
    moved = move()
    moves, lives = life(moved, moves, lives)
    win = interact(position, land, fish, lives)
    if win == 'win':
        print("Congratulations, you completed the game is {} moves!".format(moves))
    else:
        pass
    
 
