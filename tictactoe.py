import random # For random toss

board = {'topL':' ','topM':' ','topR':' ',
         'midL':' ','midM':' ','midR':' ',
         'lowL':' ','lowM':' ','lowR':' '}
# Defined a dictionary that represents the tic Tac toe board, initially it is empty

XO = False # For toggle, i.e. when X do turn next should be O's turn
oneTime = False # when all options are used it becomes True
left = [] # A list for storing options that are left to be used.

def printBoard():
    global board
    print(' '+board['topL']+' | '+board['topM']+' | '+board['topR'])
    print('---+---+---')
    print(' '+board['midL']+' | '+board['midM']+' | '+board['midR'])
    print('---+---+---')
    print(' '+board['lowL']+' | '+board['lowM']+' | '+board['lowR'])

#printBoard(board)

def optionsLeft():
    global board, left, oneTime
    print('Options that are left are ...')
    for i in board:
        if board[i] == ' ':
            print(i,',', end='')
            if oneTime == False:
                left.append(i)
    oneTime = True
    print()

def turn():
    global XO
    toss = random.randint(0,1)
    if toss == 0:
        #print('X\'s turn')
        XO = False
    else:
        #print('O\'s turn')
        XO = True

def winDecision():
    global board
    decision = False
    if ((board['topL']=='X' and board['topM']=='X' and board['topR']=='X')
        or (board['midL']=='X' and board['midM']=='X' and board['midR']=='X')
        or (board['lowL']=='X' and board['lowM']=='X' and board['lowR']=='X')
        or (board['topL']=='X' and board['midL']=='X' and board['lowL']=='X')
        or (board['topM']=='X' and board['midM']=='X' and board['lowM']=='X')
        or (board['topR']=='X' and board['midR']=='X' and board['lowR']=='X')
        or (board['topL']=='X' and board['midM']=='X' and board['lowR']=='X')
        or (board['lowR']=='X' and board['midM']=='X' and board['topR']=='X')):
        print('X wins')
        decision = True
    if ((board['topL']=='O' and board['topM']=='O' and board['topR']=='O')
        or (board['midL']=='O' and board['midM']=='O' and board['midR']=='O')
        or (board['lowL']=='O' and board['lowM']=='O' and board['lowR']=='O')
        or (board['topL']=='O' and board['midL']=='O' and board['lowL']=='O')
        or (board['topM']=='O' and board['midM']=='O' and board['lowM']=='O')
        or (board['topR']=='O' and board['midR']=='O' and board['lowR']=='O')
        or (board['topL']=='O' and board['midM']=='O' and board['lowR']=='O')
        or (board['lowR']=='O' and board['midM']=='O' and board['topR']=='O')):
        print('O wins')
        decision = True
    return decision

        
def play():
    global board, XO, left
    turn()
    print(left)
    while True:
        if XO == False:
            while True:
                print()
                print('X\'s turn')
                print()
                printBoard()
                print()
                optionsLeft()
                Entered = input()
                if Entered in left:
                    board[Entered] = 'X'
                    left.remove(Entered)
                    print(left)
                    break
                else:
                    continue
            if winDecision() == True:
                return print('Game Over')
            elif left == []:
                return print('Game Draw')
            XO = not XO
        if XO == True:
            while True:
                print()
                print('O\'s turn')
                print()
                printBoard()
                print()
                optionsLeft()
                Entered = input()
                if Entered in left:
                    board[Entered] = 'O'
                    left.remove(Entered)
                    print(left)
                    break
                else:
                    continue
            if winDecision() == True:
                return print('Game Over')
            elif left == []:
                return print('Game Draw')
            XO = not XO
    return print('Game Over')

print('Enter \'play()\' to Start play # ...')
#play()
        
