def main():
    print_grid()
    make_a_move()

def print_grid():
    print("---------")
    print(f'| {tictactoe[0][0]} {tictactoe[0][1]} {tictactoe[0][2]} |')
    print(f'| {tictactoe[1][0]} {tictactoe[1][1]} {tictactoe[1][2]} |')
    print(f'| {tictactoe[2][0]} {tictactoe[2][1]} {tictactoe[2][2]} |')
    print("---------")


def game_over():
    blanks_found = any([i for j in tictactoe for i in j if i == ' '])
    if blanks_found is False:
        return True
    else:
        return False


def make_a_move():
    cell_1 = 0
    cell_2 = 0
    requirements = False
    current_gamer = 'X'
    while game_over() is False:
        requirements = False

        while requirements is False:
            try:
                cell_1, cell_2 = map(int, input().split())
            except ValueError:
                print("You should enter numbers!")
                continue
            if cell_1 not in range(1, 4) or cell_2 not in range(1, 4):
                print("Coordinates should be from 1 to 3!")
                continue
            if tictactoe[cell_1 - 1][cell_2 - 1] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                requirements = True
                tictactoe[cell_1 - 1][cell_2 - 1] = current_gamer
                print_grid()
            if current_gamer == 'X':
                current_gamer = 'O'
            else:
                current_gamer = 'X'
    else:
        check_tictactoe()

def check_tictactoe():
    row1 = [tictactoe[0][0], tictactoe[0][1], tictactoe[0][2]]
    row2 = [tictactoe[1][0], tictactoe[1][1], tictactoe[1][2]]
    row3 = [tictactoe[2][0], tictactoe[2][1], tictactoe[2][2]]
    column1 = [tictactoe[0][0], tictactoe[1][0], tictactoe[2][0]]
    column2 = [tictactoe[0][1], tictactoe[1][1], tictactoe[2][1]]
    column3 = [tictactoe[0][2], tictactoe[1][2], tictactoe[2][2]]
    diagonal1 = [tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]]
    diagonal2 = [tictactoe[2][0], tictactoe[1][1], tictactoe[0][2]]
    win_combos = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
    message = ''
    for combos in win_combos:
     if combos.count('X') >= 3:
        message = 'X wins'
     elif combos.count('O') >= 3:
        message = 'O wins'
     elif combos.count('X') <= 3 and combos.count('O') <= 2:
        message = 'Draw'
    return print(message)



empty_grid = list(' ' * 9)
tictactoe = [empty_grid[i:i + 3] for i in range(0, len(empty_grid), 3)]

if __name__ == '__main__':
    main()