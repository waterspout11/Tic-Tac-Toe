

def print_field():  # print result of game
    print('---------')
    print('|', field_list[0][0], field_list[0][1], field_list[0][2], '|')
    print('|', field_list[1][0], field_list[1][1], field_list[1][2], '|')
    print('|', field_list[2][0], field_list[2][1], field_list[2][2], '|')
    print('---------')


def check_player_win(player):  # player 'X' or 'O'
    player_win = False
    if field_list[0][0] == field_list[0][1] == field_list[0][2] == player:
        player_win = True
    elif field_list[1][0] == field_list[1][1] == field_list[1][2] == player:
        player_win = True
    elif field_list[2][0] == field_list[2][1] == field_list[2][2] == player:
        player_win = True
    elif field_list[0][0] == field_list[1][0] == field_list[2][0] == player:
        player_win = True
    elif field_list[0][1] == field_list[1][1] == field_list[2][1] == player:
        player_win = True
    elif field_list[0][2] == field_list[1][2] == field_list[2][2] == player:
        player_win = True
    elif field_list[0][0] == field_list[1][1] == field_list[2][2] == player:
        player_win = True
    elif field_list[0][2] == field_list[1][1] == field_list[2][0] == player:
        player_win = True

    return player_win


def enter_coordinates(player_name):  # enter coordinates, check them and move on field_list
    while True:
        numbers = '0123456789'
        coord_x, coord_y = input('Enter the coordinates: > ').split(' ')
        if coord_x not in numbers or coord_y not in numbers:
            print('You should enter numbers!')
        else:
            coord_x = int(coord_x)
            coord_y = int(coord_y)
            if (coord_x > 3 or coord_x < 1) or (coord_y > 3 or coord_y < 1):
                print('Coordinates should be from 1 to 3!')
            else:
                coord_x = coord_x - 1
                coord_y = 3 - coord_y
                if field_list[coord_y][coord_x] == 'X' or field_list[coord_y][coord_x] == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    field_list[coord_y][coord_x] = player_name
                    break


def check_game_result():
    if abs(field_list.count('X') - field_list.count('O')) < 2:
        if (win_x == True and win_o == True):
            result_game = 'Impossible'
        elif win_x == True and win_o == False:
            result_game = 'X wins'
        elif win_x == False and win_o == True:
            result_game = 'O wins'
        elif win_x == False and win_o == False:
            if count_empty_place() != 0:
                result_game = 'Game not finished'
            elif count_empty_place() == 0:
                result_game = 'Draw'
    elif abs(field_list.count('X') - field_list.count('O')) >= 2:
        result_game = 'Impossible'
    return result_game

def count_empty_place(): # check how many empty place in game field
    empty_sum = 0
    for elements in field_list:
        empty_sum += elements.count(' ')
    return empty_sum


# main module
count = 1
result = ''
field_list = [[' ' for j in range(3)] for i in range(3)]
while True:
    print_field()

    if count % 2 == 0:
        enter_coordinates('O')
    elif count % 2 == 1:
        enter_coordinates('X')
    count += 1
    print('count _', field_list.count('X'))
    win_x = check_player_win('X')
    win_o = check_player_win('O')
    check_game_result()
    result = check_game_result()
    if 'win' in result or result == 'Draw':
        print_field()
        print(result)
        break