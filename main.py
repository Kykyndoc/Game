def greet():
    print("--------------------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("--------------------------------")
    print(" Формат ввода: числа от 1 - 9 ")
    print()

def get_step():
    while True:
        step = input(f'Игрок за {symbol}, ваш ход: ')
        if not step.isdigit():
            print(" Введите число! ")
            continue
        step = int(step)
        if step not in maps:
            print(" Введите номер свободной ячейки! ")
            continue
        return step

greet()
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]
count = 0

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
    print()

def step_maps(step,symbol):
    step = int(step)
    idx = step - 1
    maps[idx] = symbol

def result():
    win = ""

    for i in victory:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "0" and maps[i[1]] == "0" and maps[i[2]] == "0":
            win = "0"

    return win

game_over = False
player1 = True

while game_over == False:
    count += 1
    print_maps()
    symbol = 'X' if player1 else '0'
    step = get_step()
    step_maps(step, symbol)
    win = result()
    if win != "":
        game_over = True
        print("Победил", win)
        print_maps()
    else:
        game_over = False

    player1 = not(player1)
    if count == 9 and game_over == False:
        print(" Ничья!")
        print_maps()
        break



