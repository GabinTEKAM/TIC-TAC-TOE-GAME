""" List of functions used to realize tic tac toe game"""
import os
def clear():
    os.system( 'cls' )

def let_player():
    global player1
    global player2
    player1 = ''
    while not player1:
        player1 = input(' Player 1 are you X or O?  ').upper()
        if player1 == 'X':
            player2 = "O"
        elif player1 == "O":
            player2 = "X"
        else:
            player1 = ""

def start():
    print('Player1 will go first ')
    first_player = input('Are you ready to play?    Enter Yes or No  ').capitalize()
    if first_player.capitalize() == 'Yes':
        order = [player1 if not i %2 else player2 for i in range(9)]
    if first_player.capitalize() == 'No':
        print("Player2  will play first! ")
        order = [player2 if not i %2 else player1 for i in range(9)]
    return order


    
table = ["*" for i in range(9)]
def board():
    a = 8
    while a >= 2 :
        print ('{0}    |    {1}|    {2} '.format(table[a-2], table[a-1], table[a]))
        print ('-------------------')
        a -= 3



def win(table):
    for i in range(3):
        if  table[i] == table[i+3] == table[i+6] == "X" or table[i] == table[i+3] == table[i+6] == "O":
            print('congratulation you win!!! ')
            return True 
    for i in range (0,7,3):
        if  table[i] == table[i+1] == table[i+2] == "X" or table[i] == table[i+1] == table[i+2] == "O":
            print('congratulation you win!!! ')
            return True 
    if  table[0] == table[4] == table[8] == "X" or table[2] == table[i+1] == table[i+2] == "O":
        print('congratulation you win!!! ')
        return True 
    return False 


def board_full (table):
    if '*' in table:
        return False
    return True

def next_position(order):
    position = int(input("Enter the next position:  "))
    while not  table[position - 1 ] == '*':
        position = int(input("Enter the next position:  "))
    table[position - 1 ] = order
 