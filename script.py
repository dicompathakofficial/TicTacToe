# -------------------------------------------------------

# Vertical and horizontal checks [DONE]
# Diagonal checks from left and right side [DONE]
# Actions when no condition is met [DONE]
# User input feature [DONE]
# Game over along with making the computer wanna win [DONE]
# Improvement in the random function and
# for the computer to make more strategic moves [DONE]
# Create a GUI

# --------------------------------------------------------


import random


class GameFunctions:

    @staticmethod
    def view_grid(lst):
        for item in range(len(lst)):
            print(lst[item])
        print("------------")

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
    def random_move(lst):
        for index in range(len(lst)):
            for inner_index in range(len(lst[0])):
                if lst[index][inner_index] != 1 and lst[index][inner_index] != 2:
                    lst[index][inner_index] = 2
                    return

    @staticmethod
    def horizontal_check(lst, player, computer, player_count, computer_count):
        for item in range(len(lst)):
            if GameFunctions.count(lst[item], player) == player_count \
                    and GameFunctions.count(lst[item], computer) == computer_count:
                for num in range(len(lst[item])):
                    if lst[item][num] != 1 and lst[item][num] == 0:
                        lst[item][num] = 2
                        break  # stops the function once it finds a line that meets the condition

    @staticmethod
    def vertical_check(lst, player, computer, player_count, computer_count):
        for i in range(len(lst[0])):
            vertical_lst = []
            for num in range(len(lst)):
                vertical_lst.append(lst[num][i])
            if GameFunctions.count(vertical_lst, player) == player_count \
                    and GameFunctions.count(vertical_lst, computer) == computer_count:
                for n in range(len(lst)):
                    if lst[n][i] != 1 and lst[n][i] == 0:
                        lst[n][i] = 2
                        break

    @staticmethod
    def diagonal_check_left(lst, player, computer, player_count, computer_count):
        for i in range(len(lst[0])):
            diagonal_lst_left = []
            for num in range(len(lst)):
                diagonal_lst_left.append(lst[num][num])
            if GameFunctions.count(diagonal_lst_left, player) == player_count \
                    and GameFunctions.count(diagonal_lst_left, computer) == computer_count:
                for n in range(len(lst)):
                    if lst[n][n] != 1 and lst[n][n] == 0:
                        lst[n][n] = 2
                        return

    @staticmethod
    def diagonal_check_right(lst, player, computer, player_count, computer_count):
        diagonal_lst_right = []
        count = len(lst) - 1
        while count >= 0:
            for num in range(len(lst[0])):
                diagonal_lst_right.append(lst[count][num])
                count -= 1
        if GameFunctions.count(diagonal_lst_right, player) == player_count \
                and GameFunctions.count(diagonal_lst_right, computer) == computer_count:
            new_count = len(lst) - 1
            while new_count >= 0:
                for n in range(len(lst[0])):
                    if lst[new_count][n] != 1 and lst[new_count][n] == 0:
                        lst[new_count][n] = 2
                        return
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
        count = len(lst) - 1
        while count >= 0:
            for num in range(len(lst[0])):
                diagonal_lst_right.append(lst[count][num])
                count -= 1
        if GameFunctions.count(diagonal_lst_right, player) == 3:
            return True


grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

GameFunctions.view_grid(grid)

while True:
    u_grid = int(input("Grid?? PRESS(0 OR 1 OR 2)"))
    u_index = int(input("Index?? PRESS(0 OR 1 OR 2)"))
    if grid[u_grid][u_index] == 0:
        grid[u_grid][u_index] = 1
    else:
        print("Not Valid")
    count = GameFunctions.box_count(grid)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.horizontal_check(grid, 1, 2, 0, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.vertical_check(grid, 1, 2, 0, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_left(grid, 1, 2, 0, 2)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_right(grid, 1, 2, 0, 2)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.horizontal_check(grid, 1, 2, 2, 0)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.vertical_check(grid, 1, 2, 2, 0)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_left(grid, 1, 2, 2, 0)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_right(grid, 1, 2, 2, 0)

    if GameFunctions.box_count(grid) == count:
        GameFunctions.horizontal_check(grid, 1, 2, 0, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.vertical_check(grid, 1, 2, 0, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_left(grid, 1, 2, 0, 1)
    if GameFunctions.box_count(grid) == count:
        GameFunctions.diagonal_check_right(grid, 1, 2, 0, 1)

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
