'''
This is a side project by Pranav Shridhar and Sandeep Pillai to implement ML to beat a basic game of
tic tac toe, using re-inforced learning tactics.
'''
while(True):
    gameboard = {'7':' ','8':' ','9':' ',
                 '4':' ','5':' ','6':' ',   # This is how the basic board looks like, analogue to the numpad.
                 '1':' ','2':' ','3':' '}

    print("\n"*100, "Welcome to Tic-Tac Toe! Use your numpad to input the blocks!")


    def showboard():       #function prints the board - commend Sandeep for beautification.
        print('\n')
        print('='*13)
        print('|',gameboard['7'],'|',gameboard['8'],'|',gameboard['9'] , '|')
        print('-------------')
        print('|', gameboard['4'],'|',gameboard['5'],'|',gameboard['6'] ,'|')
        print('-------------')
        print('|', gameboard['1'],'|',gameboard['2'],'|',gameboard['3'], '|')
        print('='*13)
        print('\n')


    def win_check(gb,t):    # Lazy brute force coded logic. - blame Pranav.
        return (
            (gb['7']==t and gb['8']==t and gb['9']==t) or
            (gb['4']==t and gb['5']==t and gb['6']==t) or
            (gb['1']==t and gb['2']==t and gb['3']==t) or
            (gb['7']==t and gb['4']==t and gb['1']==t) or
            (gb['8']==t and gb['5']==t and gb['2']==t) or
            (gb['9']==t and gb['6']==t and gb['3']==t) or
            (gb['7']==t and gb['5']==t and gb['3']==t) or
            (gb['9']==t and gb['5']==t and gb['1']==t)
        )

    turn='X'
    check_list = []

    for i in range(9):
        showboard()
        print('Your Turn, player',turn, '! \nUse the numpad!')
        move = input()

        while True:
            if move not in gameboard.keys():
                print('Invalid position. Please enter again.')
                move = input()
            elif move in check_list:
                print('That position is already taken. Please enter another.')
                move = input()
            else:
                break

        gameboard[move] = turn
        check_list.append(move)
        print('\n'*42)  # Newlines between each turn.

        if win_check(gameboard,turn)==True:
            showboard()
            print(f'Player {turn} has won the game!')
            break

        if turn == 'X':
            turn = 'O'        # Swaps the player playing after each turn.
        else:
            turn = 'X'
    if i == 8:
        showboard()
        print("\nGame is a draw!!")
    if (input("\n\nPress 5 to exit, any other key to play again!")) == '5':
        break
    del gameboard # To reset game board.
