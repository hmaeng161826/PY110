import random
import os

WINNING_LINES = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], 
                [1,5,9], [3,5,7]]
INITIAL_MARKER = ' '
USER_MARKER = 'O'
COMPUTER_MARKER = 'X'
WINNING_SCORE = 5


def display_board(board):
    os.system('clear')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')

def initialize_board():
    return {square:INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==>{message}')

def empty_squares(board):
    return [key for key, value in board.items() 
            if value == INITIAL_MARKER]

def user_play(board):
    available_slots = empty_squares(board)
    while True:
        user_input = int(input(f'==>Please choose slot from {available_slots}: '))
        if user_input not in available_slots:
            prompt(f'Invalid Choice. Please enter slot number from {available_slots}.')
        else:
            board[user_input] = USER_MARKER
            break

def computer_play(board):
    available_slots = empty_squares(board)
    if len(available_slots) != 0:
        computer_input = random.choice(empty_squares(board))
        board[computer_input] = COMPUTER_MARKER


def board_full(board):
    if INITIAL_MARKER not in board.values():
        return True
    else:
        return False

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        seq1, seq2, seq3 = line
        if(board[seq1] == USER_MARKER 
                and board[seq2] == USER_MARKER
                and board[seq3] == USER_MARKER):
            return 'User'
        elif(board[seq1] == COMPUTER_MARKER 
                and board[seq2] == COMPUTER_MARKER
                and board[seq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def detect_grandwinner(score):
    if score['User'] == WINNING_SCORE:
        return 'User'
    elif score['Computer'] == WINNING_SCORE:
        return 'Computer'
    return None

def start_round(score):
    board = initialize_board()
    display_board(board)
    '''
    prompt('Welcome to Tic Tac Toe!')
    prompt('Tic Tac Toe is a 2-player game played on a 3x3 '
    'grid called the board.')
    prompt('You and Computer will take a turn and marks a square '
    'on the board.')
    prompt('The first player to get 3 squares in a row -- '
    'horizontally, vertically, or diagonally -- wins.')
    prompt('If all 9 squares are filled and neither player has 3 in '
    'a row, the game ends in a tie.')
    prompt(f"You are '{USER_MARKER}', Computer is '{COMPUTER_MARKER}'.")
    prompt(f'The current score of User vs Computer is' 
                f' {score['User']} : {score['Computer']}.')'''

    while True:
        user_play(board)
        if someone_won(board) or board_full(board):
            display_board(board)
            break
        computer_play(board)
        if someone_won(board) or board_full(board):
            display_board(board)
            break
        display_board(board)

    if someone_won(board):
        prompt(f"The winner is '{detect_winner(board)}'!")
        score[detect_winner(board)] += 1
        prompt(f"The current score of User vs Computer is"
            f" {score['User']} : {score['Computer']}.")
     
    else:
        prompt("It's a tie!")
        prompt(f'The current score of User vs Computer is' 
            f' {score['User']} : {score['Computer']}.')

        
def play_tictactoe():
    while True:
        score = {
        'User' : 0,
        'Computer': 0
        }
        while not detect_grandwinner(score):
            start_round(score)

        while True:    
            prompt('Would you like to play another game? (Y/N): ')
            user_response = input().lower()
            if user_response == 'n' or user_response == 'no':
                prompt('Thanks for playing Tic Tac Toe! Goodbye :) ')
                break
            elif user_response != 'y' or user_response != 'yes':
                prompt('Invalid Input. Please enter Y to play another game or'
                    'N to exit')

play_tictactoe()