import random

print('Tic Tac Toe:')
pos = 0
turn = 1
autovalid = False
random_number = 0

gamestate = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def rng(random_number, gamestate, autovalid, choice_list):
    autovalid = False
    while autovalid == False:
        random_number = random.randint(0, 8)
        if gamestate[random_number] == '-':
            gamestate[random_number] = choice_list[1]
            autovalid = True
        else:
            autovalid = False
    return gamestate

def move_validity(pos, gamestate): # Tests move valitdity
    if str(gamestate[pos]) != '-':
        print('Invalid move, please try again')
        valid = False
        return valid
    else:
        valid = True
        return valid

def choice_symbol(choice):
    choice = input('X or O: ')
    if not choice.isalpha():
        print('Please try again, invalid symbol entered. Pick between X and O.')
        return choice_symbol(choice)
    elif choice.upper() == 'X':
        choice_rng = 'O'
    elif choice.upper() == 'O':
        choice_rng = 'X'
    else:
        print('Something really went wrong, try to pick between X and O.')
        return choice_symbol(choice)
    return [choice.upper(), choice_rng]

def display_board(gamestate):
    # Printing gamestate in such a way that it looks like a Tic Tac Toe Board
    print(gamestate[0:3])
    print(gamestate[3:6])
    print(gamestate[6:9])

def update(pos, turn, gamestate, choice_list): # Updates the gamestate
        if int(turn) == int(1):
            gamestate[int(pos)] = choice_list[0]
            return gamestate
        elif int(turn) == int(2):
            gamestate[int(pos)] = choice_list[1]
            return gamestate
        else:
            ('ERROR') # Error case
def check_win(gamestate): # Win Cases
# I have to make sure that the values of the gamestate that register as a win aren't just a series of dashes, which is why I specify " != '-' "
# Horizontal win cases
        if gamestate[0] == gamestate[1] == gamestate[2] != '-' or gamestate[3] == gamestate[4] == gamestate[5] != '-' or gamestate[6] == gamestate[7] == gamestate[8] != '-':
            win = True
            return win
# Vertical win cases
        elif gamestate[0] == gamestate[3] == gamestate[6] != '-' or gamestate[1] == gamestate[4] == gamestate[7] != '-' or gamestate[2] == gamestate[5] == gamestate[8] != '-':
            win = True
            return win
# Diagonal win cases
        elif gamestate[0] == gamestate[4] == gamestate[8] != '-' or gamestate[2] == gamestate[4] == gamestate[6] != '-':
            win = True
            return win
# No win case
        else:
            win = False
            return win
def restart():
    gamestate = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turn = 1
    win = False
    return gamestate, turn, win
def choose_position(): # This function asks for a players choice
    pos = input('Player ' + str(turn) + ': ')
    if not pos.isnumeric():
        print('Invalid move, need to pick a number from 0 - 8 (including 0 and 8).')
        return choose_position()
    elif not 0 <= int(pos) <= 8:
        print('Invalid move, need to pick a number from 0 - 8 (including 0 and 8).')
        return choose_position()
    else:
        return int(pos)
    
    
def Tic_Tac_Toe():
    global gamestate
    global pos
    global turn
    global choice_list
    
    choice = None
    choice_list = choice_symbol(choice)
    
    while True:
        # Player 1:
        if turn == 1:
            display_board(gamestate) # Prints out the tic tac toe board
            pos = choose_position() # Takes the player's input
            
            # Checks move validity
            valid = move_validity(pos, gamestate)
            if valid == True:
                gamestate = update(pos, turn, gamestate, choice_list)
            if valid == False:
                while valid == False:
                    pos = choose_position()
                    valid = move_validity(pos, gamestate)

            # Checks for a win
            win = check_win(gamestate)
            if win == True:
                print('Player wins! \n')
                display_board(gamestate) # Shows the board as someone has won
                break

            turn = 2 # Changes the turn for the robot
            
            # Checks for a tie:
            if '-' not in gamestate:
                print('Tie game.')
                break

        # Robot's turn:
        if turn == 2:

            # Making a valid move:
            gamestate = rng(random_number, gamestate, autovalid, choice_list)

            # Checks for a win
            win = check_win(gamestate)
            if win == True:
                print('The robot wins! \n')
                display_board(gamestate) # Shows the board as someone has woncl
                break

            turn = 1 # Changes the turn for the other player
            print('---------------') # Empty space so it looks better
            # Checks for a tie:
            if '-' not in gamestate:
                print('Tie game.')
                break

Tic_Tac_Toe() # Starts the first game

# Allows you to choose whether you want to play another game or not.
restart_case = input(' \n y/n Would you like to play again? ')
if restart_case == 'y':
    gamestate, turn, win = restart()
    print('')
    Tic_Tac_Toe()
