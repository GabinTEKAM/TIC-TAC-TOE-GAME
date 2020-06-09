from functions import *

def play():
    replay = True
    while replay:
        let_player()
        order = start()
        board()
    
        a = 0
        while  a < 9 :
            next_position( order[a])
            a += 1
            clear()
            board()
            if win(table):
                break
        if  board_full(table):
            print('Game over!')
        play = ''
        while play != 'Yes' and play != 'No':
            play = input('Do you want to replay: Yes or NO  ').capitalize()
        if play == 'Yes':
            replay = True
        else:
            replay = False


play()