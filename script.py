# Vertical and horizontal checks [DONE]
# Diagonal checks from left and right side are left [DONE]
# Making the initial move is left [DONE]
# Actions when no condition is met is left [DONE]
# User input feature is left [DONE]
# Game over is not done yet along with making computer wanna win
# Convert the code to pycharm

import random


class GameFunctions:

    @staticmethod
    def view_grid(lst):
        for item in range(len(lst)):
            print(lst[item])

    @staticmethod
    def count(lst, item):
        count = 0
        for items in lst:
            if item == items:
                count += 1
        return count

    @staticmethod
    def box_count(lst):
        count = 0
        for num in range(len(lst)):
            for num_inner in range(len(lst)):
                if lst[num][num_inner] != 0:
                    count += 1
        return count

    @staticmethod
    def initial_move(lst):
        random_vertical_row = random.randint(0, 2)
        random_horizontal_row = random.randint(0, 2)
        if lst[random_vertical_row][random_horizontal_row] != 1:
            lst[random_vertical_row][random_horizontal_row] = 2
        return

    @staticmethod
    def random_move(lst):
        for index in range(len(lst)):
            for inner_index in range(len(lst[0])):
                if lst[index][inner_index] != 1 and lst[index][inner_index] != 2:
                    lst[index][inner_index] = 2
                    return

    @staticmethod
    def horizontal_check(lst, player, computer):
        for item in range(len(lst)):
            if GameFunctions.count(lst[item], player) == 2 and GameFunctions.count(lst[item], computer) == 0:
                for num in range(len(lst[item])):
                    if lst[item][num] != 1:
                        lst[item][num] = 2
                break  # stops the function once it finds a line that meets the condition

    @staticmethod
    def vertical_check(lst, player, computer):
        for i in range(len(lst[0])):
            vertical_lst = []
            for num in range(len(lst)):
                vertical_lst.append(lst[num][i])
            if GameFunctions.count(vertical_lst, player) == 2 and GameFunctions.count(vertical_lst, computer) == 0:
                for n in range(len(lst)):
                    if lst[n][i] != 1:
                        lst[n][i] = 2
                break

    @staticmethod
    def diagonal_check_left(lst, player, computer):
        diagonal_lst_left = []
        for num in range(len(lst)):
            diagonal_lst_left.append(lst[num][num])
        if GameFunctions.count(diagonal_lst_left, player) == 2 and GameFunctions.count(diagonal_lst_left,
                                                                                       computer) == 0:
            for n in range(len(lst)):
                if lst[n][n] != 1:
                    lst[n][n] = 2

    @staticmethod
    def diagonal_check_right(lst, player, computer):
        diagonal_lst_right = []
        count = len(lst) - 1
        while count >= 0:
            for num in range(len(lst[0])):
                diagonal_lst_right.append(lst[count][num])
                count -= 1
        if GameFunctions.count(diagonal_lst_right, player) == 2 and GameFunctions.count(diagonal_lst_right,
                                                                                        computer) == 0:
            new_count = len(lst) - 1
            while new_count >= 0:
                for n in range(len(lst[0])):
                    if lst[new_count][n] != 1:
                        lst[new_count][n] = 2
                    new_count -= 1

    @staticmethod
    def win_check(lst, player):
        for item in range(len(lst)):
            if GameFunctions.count(lst[item], player) == 3:
                return True

        for i in range(len(lst[0])):
            vertical_lst = []
            for num in range(len(lst)):
                vertical_lst.append(lst[num][i])
            if GameFunctions.count(vertical_lst, player) == 3:
                return True

        diagonal_lst_left = []
        for num in range(len(lst)):
            diagonal_lst_left.append(lst[num][num])
        if GameFunctions.count(diagonal_lst_left, player) == 3:
            return True

        diagonal_lst_right = []
        counting = len(lst) - 1
        while counting >= 0:
            for num in range(len(lst[0])):
                diagonal_lst_right.append(lst[counting][num])
                counting -= 1
        if GameFunctions.count(diagonal_lst_right, player) == 3:
            return True




grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
GameFunctions.initial_move(grid)
GameFunctions.view_grid(grid)

print("-------------------------")

while True:  # currently an infinite loop / only loops out when game is over
    u_grid = int(input("Grid??"))
    u_index = int(input("Index??"))
    if grid[u_grid][u_index] == 0:
        grid[u_grid][u_index] = 1
    else:
        print("Not Valid")  # re asking for input if input not valid is not proper
    count = GameFunctions.box_count(grid)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.horizontal_check(grid, 2, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.vertical_check(grid, 2, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_left(grid, 2, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_right(grid, 2, 1)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.horizontal_check(grid, 1, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.vertical_check(grid, 1, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_left(grid, 1, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_right(grid, 1, 2)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.random_move(grid)

    if GameFunctions.win_check(grid, 2):
        GameFunctions.view_grid(grid)
        print("Player Lost!!!!")
        break
    if GameFunctions.win_check(grid, 1):
        GameFunctions.view_grid(grid)
        print("Player Wins!!!!!")
        break

    if GameFunctions.box_count(grid) == 9:
        GameFunctions.view_grid(grid)
        print("Game Tied!!!!!")
        break

    GameFunctions.view_grid(grid)
