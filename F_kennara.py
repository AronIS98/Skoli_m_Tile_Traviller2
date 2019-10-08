import random
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1  # (3,1)


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def lever(money):
    lever = print("Pull a lever (y/n): ",end="")
    y_n = ["y","n"]
    lever = random.choice(y_n)
    print(lever)
    if lever == "y" or lever == "Y":
        money += 1
        print("You received 1 coin, your total is now {}.".format(money))
    return money


def find_directions(col, row, coin,ok,valid):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
        if ok == True:
            coin = lever(coin)
            valid+=1
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
        if ok == True:
            coin = lever(coin)
            valid+=1

    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
        if ok == True:
            coin = lever(coin)
            valid+=1
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
        if ok == True:
            coin = lever(coin)
            valid+=1
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions, coin,valid

def play_one_move(col, row, valid_directions,valid,not_valid,total_moves):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    total_moves+=1
    #direct = ["n","e","s","w"]
    victory = False
    direction = print("Direction: ",end = "")
    direction = random.choice(["n","e","s","w"])
    print(direction)
    direction = direction.lower()

    if not direction in valid_directions:
        print("Not a valid direction!")
        ok = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        valid += 1
        ok = True
    return victory, col, row,valid,not_valid,ok,total_moves


# The main program starts here
victory = False
row = 1
col = 1
money = 0
check = 1
valid=0
not_valid=0
total_moves = 0
seed = int(input("Input seed: "))
random.seed(seed)
valid_directions = NORTH
print_directions(valid_directions)
ok = True
while check == 1:
    
    victory, col, row,valid,not_valid,ok,total_moves = play_one_move(col, row, valid_directions,valid,not_valid,total_moves)
    if victory:
        print("Victory! ", end="")
        print("Total coins {}. Moves {}.".format(money,total_moves))
        cont = ["y","n"]
        continue_input = input('Play again (y/n): ')
        continue_input.lower()
        if continue_input is 'y':
            money = 0
            row = 1
            col = 1
            valid_directions = NORTH
            print_directions(valid_directions)
        else:
            check = 0

    else:
        valid_directions, money,valid = find_directions(col, row, money,ok,valid)
        print_directions(valid_directions)
