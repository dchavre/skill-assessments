print('Tic Tac Toe:')
pos = 0
turn = 1

gamestate = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def display_board(gamestate):
    # Printing gamestate in such a way that it looks like a Tic Tac Toe Board
    print(gamestate[0:3])
    print(gamestate[3:6])
    print(gamestate[6:9])
def move_validity(pos, gamestate): # Tests move valitdity
    if str(gamestate[int(pos)]) != '-':
        print('Invalid move, please try again')
        valid = False
        return valid
    else:
        valid = True
        return valid
def update(pos, turn, gamestate): # Updates the gamestate
        if int(turn) == int(1):
            gamestate[int(pos)] = 'X'
            return gamestate
        elif int(turn) == int(2):
            gamestate[int(pos)] = 'O'
            return gamestate
        else:
            ('ERROR') # Error case
def check_win(turn, gamestate): # Win Cases
# I have to make sure that the values of the gamestate that register as a win aren't just a series of dashes, which is why I specify " != '-' "
# Horizontal win cases
        if gamestate[0] == gamestate[1] == gamestate[2] != '-' or gamestate[3] == gamestate[4] == gamestate[5] != '-' or gamestate[6] == gamestate[7] == gamestate[8] != '-':
            winner = turn
            win = True
            return winner, win
# Vertical win cases
        elif gamestate[0] == gamestate[3] == gamestate[6] != '-' or gamestate[1] == gamestate[4] == gamestate[7] != '-' or gamestate[2] == gamestate[5] == gamestate[8] != '-':
            winner = turn
            win = True
            return winner, win
# Diagonal win cases
        elif gamestate[0] == gamestate[4] == gamestate[8] != '-' or gamestate[2] == gamestate[4] == gamestate[6] != '-':
            winner = turn
            win = True
            return winner, win
# Error case
        else:
            winner = 'None'
            win = False
            return winner, win
def restart():
    gamestate = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turn = 1
    win = False
    return gamestate, turn, win
def choose_position(): # This function asks for a players choice
    pos = input('Player ' + str(turn) + ': ')
    if int(pos) < 0 or int(pos) > 8: # Checks to make sure that the choice they make is 0 - 8.
        print('Invalid move, need tp pick a number from 0 - 8 (including 0 and 8).')
        while pos < 0 or pos > 8:
            pos = input('Player ' + str(turn) + ': ')
            if int(pos) < 0 or int(pos) > 8:
                print('Invalid move, need tp pick a number from 0 - 8 (including 0 and 8).')
    else:
        return pos
def Tic_Tac_Toe():
    while True:
        # Making some global variable to make my life easier
        global gamestate
        global pos
        global turn

        # Player 1:
        if turn == 1:
            display_board(gamestate) # Prints out the tic tac toe board
            pos = choose_position() # Takes the player's input
            print('') # Extra space
            # Checks move validity
            valid = move_validity(pos, gamestate)
            if valid == True:
                gamestate = update(pos, turn, gamestate)
            if valid == False:
                while valid == False:
                    pos = choose_position()
                    valid = move_validity(pos, gamestate)

            # Checks for a win
            winner, win = check_win(turn, gamestate)
            if win == True:
                print('Player '+ str(winner) + ' wins! \n')
                display_board(gamestate) # Shows the board as someone has won
                break

            turn = 2 # Changes the turn for the other player
            
            # Checks for a tie:
            if '-' not in gamestate:
                print('Tie game.')
                break

        # Player 2:
        if turn == 2:
            display_board(gamestate) # Prints out the tic tac toe board
            pos = choose_position() # Takes the player's input
            
            # Checks move validity
            valid = move_validity(pos, gamestate)
            if valid == True:
                gamestate = update(pos, turn, gamestate)
            if valid == False:
                while valid == False:
                    pos = choose_position()
                    valid = move_validity(pos, gamestate)

            # Checks for a win
            winner, win = check_win(turn, gamestate)
            if win == True:
                print('Player ' + str(winner) + ' wins! \n')
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
restart_case = input(' \n y/n Would you like to play again? \n')
if restart_case == 'y':
    gamestate, turn, win = restart()
    Tic_Tac_Toe()