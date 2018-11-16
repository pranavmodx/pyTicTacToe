gameboard={'topleft':' ','topmid':' ','topright':' ',
           'midleft':' ','midmid':' ','midright':' ',
           'bottomleft':' ','bottommid':' ','bottomright':' '}
def showboard(board):
    print('\n')
    print(gameboard['topleft'],'|',gameboard['topmid'],'|',gameboard['topright'])
    print('---------')
    print(gameboard['midleft'],'|',gameboard['midmid'],'|',gameboard['midright'])
    print('---------')
    print(gameboard['bottomleft'],'|',gameboard['bottommid'],'|',gameboard['bottomright'])
    print('\n')

def win_check(gb,t):
    return (
        (gb['topleft']==t and gb['topmid']==t and gb['topright']==t) or
        (gb['midleft']==t and gb['midmid']==t and gb['midright']==t) or
        (gb['bottomleft']==t and gb['bottommid']==t and gb['bottomright']==t) or
        (gb['topleft']==t and gb['midleft']==t and gb['bottomleft']==t) or
        (gb['topmid']==t and gb['midmid']==t and gb['bottommid']==t) or
        (gb['topright']==t and gb['midright']==t and gb['bottomright']==t) or
        (gb['topleft']==t and gb['midmid']==t and gb['bottomright']==t) or
        (gb['topright']==t and gb['midmid']==t and gb['bottomleft']==t)
    )

turn='X'
check_list = []
for i in range(9):
    showboard(gameboard)
    print('Make a move, player',turn)
    move=input()
    while True:
        if move not in gameboard.keys():
            print('Invalid position. Please enter again.')
            move=input()
        elif move in check_list:
            print('That position is already taken. Please enter another.')
            move=input()
        else:
            break
    gameboard[move]=turn
    check_list.append(move)
    if win_check(gameboard,turn)==True:
        print(f'Player {turn} has won the game.')
        break
    if turn=='X':
        turn='O'
    else:
        turn='X'
showboard(gameboard)

