# maui_project_v1.py
# Created by: Simon Lee
# Created on: 18/08/2020
"""
Version 1

"""
# create variables, lists, import modules etc.
import random
lives = 3
moves = 0


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
- (U)p
- (D)own
- (L)eft
- (R)ight
Enter direction: """).lower()
    while direction not in moves:
        print("Please enter a valid move.")
        direction = input("Would you like to move: (up, down, left, right) ").lower()

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
        if moves % 2 == 0 and moves != 0:
            lives -= 1
            print("You have eaten 1 fish after your 2 moves!")
            print("You now have {} left!".format(lives))
    elif moved == 'n':
        pass
    return moves, lives

# interact function: lets user fish fish and land on the land
def interact(position, land, fish, lives):
    if position == land:
        print("Congratulations, you have found Aotearoa!")
    elif position in fish:
        print("Your fishermen have caught a massive tuna!")
        print("You now have 1 more fish, so you have a total of {}".format(lives))
        lives += 1
        fish.remove(position)

        
position, land, fish = grid()
for i in range (0,100):
    moved = move()
    moves, lives = life(moved, moves, lives)
    interact(position, land, fish, lives)
