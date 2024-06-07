import random
def gamelogics(new_list, player, player1):
    logic =[]
    if (new_list[0][0] == new_list[0][1] == new_list[0][2] == player or new_list[0][0] == new_list[1][0] ==
            new_list[2][0] == player or new_list[0][0] == new_list[1][0] == new_list[2][0] == player or new_list[0][
                0] == new_list[1][0] == new_list[2][0] == player or new_list[0][1] == new_list[1][1] == new_list[2][
                1] == player or new_list[2][0] == new_list[2][1] == new_list[2][2] == player or new_list[0][2] ==
            new_list[1][2] == new_list[2][2] == player or new_list[0][0] == new_list[1][1] == new_list[2][
                2] == player or new_list[0][2] == new_list[1][1] == new_list[2][1] == player):
        print('player1 win')
        logic = [True,player]

    elif (new_list[0][0] == new_list[0][1] == new_list[0][2] == player1 or new_list[0][0] == new_list[1][0] ==
          new_list[2][0] == player1 or new_list[0][0] == new_list[1][0] == new_list[2][0] == player1 or new_list[0][
              0] == new_list[1][0] == new_list[2][0] == player1 or new_list[0][1] == new_list[1][1] == new_list[2][
              1] == player1 or new_list[2][0] == new_list[2][1] == new_list[2][2] == player1 or new_list[0][2] ==
          new_list[1][2] == new_list[2][2] == player1 or new_list[0][0] == new_list[1][1] == new_list[2][
              2] == player or new_list[0][2] == new_list[1][1] == new_list[2][1] == player):
        print('player2 win')
        logic = [True,player1]
    else:
        logic = [False]
    return logic


def addition():
    r=int(input('enter a row num'))
    c=int(input('enter  a column num'))
    print(r,c)


num = int(input('1: 1 player \n2: 2 players'))
if num ==1:

    r = 0
    c = 0

    # player = input('choose player1 x or o')
    player1 = input('choose player x or o')
    if player1 == 'x':
        player = 'o'
    else:
        player = 'x'

    turn = 0
    new_list = [['', '', ''], ['', '', '', ], ['', '', '']]
    while True:
        i = random.randint(0, 2)
        m = random.randint(0, 2)

        if turn == 0:
            print('player turn')
            addition()
            if new_list[r][c] == '':
                new_list[(r)][(c)] = player1
                turn = 1
            for i in new_list:
                print(i)
            else:
                pass
                # print('already exists')


        else:
            print('computer turn')
            if new_list[i][m] == '':
                new_list[(i)][(m)] = player
                turn = 0
            for i in new_list:
                print(i)
            else:
                pass
                # print('already exist')
        result = gamelogics(new_list,player, player1)
        if result[0]:
            break

elif num == 2:

    r = 0
    c = 0
    player = 0
    player1 = input('choose player x or o')
    if player1 == 'x':
        player = 'o'
    elif player1 == 'o':
        player = 'x'

    turn = 0
    new_list = [['', '', ''], ['', '', '', ], ['', '', '']]
    while True:
        if turn == 0:
            print('player1 turn')
            addition()
            if new_list[r][c] == '':
                new_list[r][c] = player1
                turn = 1
            else:
                print('already exists')
                turn = 0

            for i in new_list:
                print(i)

            turn = 1
        else:
            print('player2 turn')
            addition()
            if new_list[r][c] == '':
                new_list[r][c] = player
                turn = 0
            else:
                print('already exist')
                turn = 1
            for i in new_list:
                print(i)
        if gamelogics(new_list, player, player1)[0]:
            break
else:
    print('incorrect input')



