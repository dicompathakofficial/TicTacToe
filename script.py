# Vertical and horizontal checks [DONE]
# Diagonal checks from left and right side are left [DONE]
# Making the initial move is left [DONE]
# Actions when no condition is met is left [DONE]
# User input feature is left
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
                    break

    @staticmethod
    def horizontal_check(lst):
        for item in range(len(lst)):
            if GameFunctions.count(lst[item], 1) == 2 and GameFunctions.count(lst[item], 2) == 0:
                for num in range(len(lst[item])):
                    if lst[item][num] != 1:
                        lst[item][num] = 2
                break  # stops the function once it finds a line that meets the condition

    @staticmethod
    def vertical_check(lst):
        for i in range(len(lst[0])):
            vertical_lst = []
            for num in range(len(lst)):
                vertical_lst.append(lst[num][i])
            if GameFunctions.count(vertical_lst, 1) == 2 and GameFunctions.count(vertical_lst, 2) == 0:
                for n in range(len(lst)):
                    if lst[n][i] != 1:
                        lst[n][i] = 2
                break

    @staticmethod
    def diagonal_check_left(lst):
        diagonal_lst_left = []
        for num in range(len(lst)):
            diagonal_lst_left.append(lst[num][num])
        if GameFunctions.count(diagonal_lst_left, 1) == 2 and GameFunctions.count(diagonal_lst_left, 2) == 0:
            for n in range(len(lst)):
                if lst[n][n] != 1:
                    lst[n][n] = 2

    @staticmethod
    def diagonal_check_right(lst):
        diagonal_lst_right = []
        count = len(lst) - 1
        while count >= 0:
            for num in range(len(lst[0])):
                diagonal_lst_right.append(lst[count][num])
                count -= 1
        if GameFunctions.count(diagonal_lst_right, 1) == 2 and GameFunctions.count(diagonal_lst_right, 2) == 0:
            new_count = len(lst) - 1
            while new_count >= 0:
                for n in range(len(lst[0])):
                    if lst[new_count][n] != 1:
                        lst[new_count][n] = 2
                    new_count -= 1


grid = [
    [1, 2, 1],
    [1, 1, 2],
    [2, 2, 2]
]

GameFunctions.view_grid(grid)

print("-------------------------")

#GameFunctions.initial_move(grid)
GameFunctions.random_move(grid)

GameFunctions.view_grid(grid)



