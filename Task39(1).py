import random

playground = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_playground():
    print(playground[0], end=" ")
    print(playground[1], end=" ")
    print(playground[2])

    print(playground[3], end=" ")
    print(playground[4], end=" ")
    print(playground[5])

    print(playground[6], end=" ")
    print(playground[7], end=" ")
    print(playground[8])

def check_victories():
    for i in victories:
        if playground[i[0]] == playground[i[1]] == playground[i[2]]:
            return True
    return False

print_playground()
name1 = input("Введите имя первого игрока -  ")
name2 = input("Введите имя второго игрока -  ")

first_turn = random.choice([name1,name2])

cur_turn = first_turn

count = 0

while True:
    print(f"сейчас ходит {cur_turn}")
    if cur_turn==first_turn:
        symbol = "X"
        step = int(input("введи клетку от 1 до 9, куда хочешь походить "))
        if playground[step-1] in ["X","0"]:
            print("клетка занята")
            continue
        playground[step-1] = symbol
    else:
        symbol = "O"
        step = int(input("введи клетку от 1 до 9, куда хочешь походить "))
        if playground[step - 1] in ["X", "0"]:
            print("клетка занята")
            continue
        playground[step - 1] = symbol
    print_playground()
    if check_victories():
        print(f"победил игрок {cur_turn}")
        break
    count+=1
    cur_turn = name2 if cur_turn == name1 else name1
    if count == 9:
        print("Ничья")
        break