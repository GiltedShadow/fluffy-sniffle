"""
Created by Alex Norment
started on 2.22.2024
the goal is to create a finctional tic tac toe board from the
 Zero to Hero Python course milestone 1 project
this will actually be technically a "rewite" as I've created one in the past
 but this program will be completely new and only reference fixes and
 how-tos from the previous program
"""

import time

playerOneIcon = 'Player One'
playerTwoIcon = 'Player Two'
pOneScore = 0
pTwoScore = 0
winscore = 0

# I plan on tracking moves available in a list and displaying via a dictionary
# The list will .pop a move when it is taken to ensure that players do not choose the same space
movesAvailable = [1,2,3,4,5,6,7,8,9]

playerMoves = {
    #possible to keep the numbers here as a display of what move is available for easy viewing
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9'
    }

board ={
    'row':('*'*17),
    'spacer':(' '*5 + '*' + ' '*5 + '*'),
    'playRow1':('  {}  *  {}  *  {}'.format(playerMoves[1], playerMoves[2], playerMoves[3])),
    'playRow2':('  {}  *  {}  *  {}'.format(playerMoves[4], playerMoves[5], playerMoves[6])),
    'playRow3':('  {}  *  {}  *  {}'.format(playerMoves[7], playerMoves[8], playerMoves[9]))
    }

def board_clear():
    global movesAvailable

    playerMoves[1]='1'
    playerMoves[2]='2'
    playerMoves[3]='3'
    playerMoves[4]='4'
    playerMoves[5]='5'
    playerMoves[6]='6'
    playerMoves[7]='7'
    playerMoves[8]='8'
    playerMoves[9]='9'
    board_update()
    display_board()
    movesAvailable = [1,2,3,4,5,6,7,8,9]


def board_update():
    board['playRow1'] = ('  {}  *  {}  *  {}'.format(playerMoves[1], playerMoves[2], playerMoves[3]))
    board['playRow2'] = ('  {}  *  {}  *  {}'.format(playerMoves[4], playerMoves[5], playerMoves[6]))
    board['playRow3'] = ('  {}  *  {}  *  {}'.format(playerMoves[7], playerMoves[8], playerMoves[9]))

def display_board():
    print(board['spacer'])
    print(board['playRow1'])
    print(board['spacer'])
    print(board['row'])
    print(board['spacer'])
    print(board['playRow2'])
    print(board['spacer'])
    print(board['row'])
    print(board['spacer'])
    print(board['playRow3'])
    print(board['spacer'])

def help_text_rules():
    print("""
    Rules:
    1/ Players will be able to select their own icons, they *must* only be 1 character long and cannot be empty
    2/ Once a move has been taken it cannot be used again until the next game
    3/ Moves are input as the number for the space
    4/ The basic ruleset for the game is the same: match 3 in a row in order to win :3

    The board you will be playing on to follow, available moves are {}
    """.format(movesAvailable))

def initial_game_start():
    global winscore
    totalScore = input("How many are you playing to?")
    try:
        totalScore = int(totalScore)
        if totalScore <= 0:
            print("Please enter a number above 0")
            initial_game_start()
        else:
            winscore = totalScore
            
    except ValueError:
        print("Please enter a valid number")
        initial_game_start()
        
def player_icon_collection(player):
    global playerOneIcon
    global playerTwoIcon
    iconTest = input("{}, what character would you like to use as your token?".format(player))
    if len(iconTest) > 1:
        print("Too many characters, please only enter one")
        player_icon_collection(player)
    elif len(iconTest) < 1:
        print("Too few characters, please enter one")
        player_icon_collection(player)
    elif iconTest.isspace():
        print("Please enter a chatacter other than a space")
        player_icon_collection(player)
    else:
        if player == playerOneIcon:
            playerOneIcon = iconTest
        elif player == playerTwoIcon:
            playerTwoIcon = iconTest

def make_a_move(player):
    if len(movesAvailable) == 0:
        print("Cat Game! Resetting board...")
        board_clear()
    move = input("player {}, what is your move?".format(player))
    try: 
        move = int(move)
        
    except ValueError:
        print("Move entered is not a number, please enter a valid move")
        make_a_move(player)
    
    if move in movesAvailable:
        for num in range(len(movesAvailable)):
            if movesAvailable[num] == move:
                playerMoves[move] = player
                movesAvailable.pop(num)
                board_update()
                display_board()
                #Test statement to ensure sucess
                #print(move)
                break

    elif move not in movesAvailable:
        print("Invalid move, please select a move within {}".format(movesAvailable))
        make_a_move(player)  

def score(player):
    global playerOneIcon
    global playerTwoIcon
    global pOneScore
    global pTwoScore
    global winscore

    if player == playerOneIcon:
        pOneScore += 1
    elif player == playerTwoIcon:
        pTwoScore += 1

    print("player {} has scored! {} -- {} vs {} -- {}".format(player, playerOneIcon, pOneScore, playerTwoIcon, pTwoScore))
    print("Playing to {}".format(winscore))
    board_clear()
    
def check_for_set_win():
    global pOneScore
    global pTwoScore
    global winscore
    global active

    if pOneScore == winscore:
        newGameSet = input("player one has won!\nWould you like to play again? (y/n):")
        active = False
        if newGameSet.lower() == 'y':
            active = True
            initial_game_start()
        #quit()
    elif pTwoScore == winscore:
        newGameSet = input("player two has won!\nWould you like to play again? (y/n):")
        active = False
        if newGameSet.lower() == 'y':
            active = True
            initial_game_start()
        #quit()

def check_for_win(player):
    """
    possible win conditons are as follows: and main board spacing:
    xxx  ---  ---  x--  --x  x--  -x-  --x        123
    ---  xxx  ---  -x-  -x-  x--  -x-  --x        456
    ---, ---, xxx, --x, x--, x--, -x-, --x,       789
    whats the easiest way to run through 8 conditions here?
    mostly I would saw 8 if/elif statements, and there isn't one specific move that needs to happen for each condition
    """
    if playerMoves[1] == player and playerMoves[2] == player and playerMoves[3] == player:  
        score(player)
    elif playerMoves[4] == player and playerMoves[5] == player and playerMoves[6] == player:
        score(player)
    elif playerMoves[7] == player and playerMoves[8] == player and playerMoves[9] == player:
        score(player)
    elif playerMoves[1] == player and playerMoves[4] == player and playerMoves[7] == player:
        score(player)
    elif playerMoves[2] == player and playerMoves[5] == player and playerMoves[8] == player:
        score(player)
    elif playerMoves[3] == player and playerMoves[6] == player and playerMoves[9] == player:
        score(player)
    elif playerMoves[1] == player and playerMoves[5] == player and playerMoves[9] == player:
        score(player)
    elif playerMoves[3] == player and playerMoves[5] == player and playerMoves[7] == player:
        score(player)

#curtosy of https://patorjk.com/software/taag/#p=display&f=3D%20Diagonal&t=Tic%20Tac%20Toe
# in order to not flood the user's terminal with the ascii art time was used to pause between words
def into_welcome_fancy():
    print("Welcome to Alex's")
    time.sleep(2)
    print("""
            ,----,                                   
          ,/   .`|                                   
        ,`   .'  :                                   
      ;    ;     / ,--,                              
    .'___,/    ,',--.'|                              
    |    :     | |  |,                               
    ;    |.';  ; `--'_       ,---.                   
    `----'  |  | ,' ,'|     /     \                  
        '   :  ; '  | |    /    / '                  
        |   |  ' |  | :   .    ' /                   
        '   :  | '  : |__ '   ; :__                  
        ;   |.'  |  | '.'|'   | '.'|                 
        '---'    ;  :    ;|   :    :                 
                 |  ,   /  \   \  /                  
                  ---`-'    `----' """)
    time.sleep(2)
    print("""
                    ,----,                           
                  ,/   .`|                           
                ,`   .'  :                           
              ;    ;     /                           
            .'___,/    ,'                            
            |    :     |                             
            ;    |.';  ;  ,--.--.      ,---.         
            `----'  |  | /       \    /     \        
                '   :  ;.--.  .-. |  /    / '        
                |   |  ' \__\/: . . .    ' /         
                '   :  | ," .--.; | '   ; :__        
                ;   |.' /  /  ,.  | '   | '.'|       
                '---'  ;  :   .'   \|   :    :       
                       |  ,     .-./ \   \  /        
                        `--`---'      `----'         """)
    time.sleep(2)
    print("""
                            ,----,                   
                          ,/   .`|                   
                        ,`   .'  :                   
                      ;    ;     /                   
                    .'___,/    ,'  ,---.             
                    |    :     |  '   ,'\            
                    ;    |.';  ; /   /   |   ,---.   
                    `----'  |  |.   ; ,. :  /     \  
                        '   :  ;'   | |: : /    /  | 
                        |   |  ''   | .; :.    ' / | 
                        '   :  ||   :    |'   ;   /| 
                        ;   |.'  \   \  / '   |  / | 
                        '---'     `----'  |   :    | 
                                           \   \  /  
                                            `----' """)
    time.sleep(2)

#into_welcome_fancy()

help_text_rules()

display_board()

initial_game_start()

player_icon_collection(playerOneIcon)

player_icon_collection(playerTwoIcon)


#start of game loop
active = True
while active:

    make_a_move(playerOneIcon)
    check_for_win(playerOneIcon)
    check_for_set_win()
    make_a_move(playerTwoIcon)
    check_for_win(playerTwoIcon)
    check_for_set_win()

#test statements below to check proper function of above
#print(playerOneIcon)
#print(playerTwoIcon)


            
#TODO: check win conditions




#TODO: check win conditions
#can this just be one function? like check_win(playerx)


#display_board()
