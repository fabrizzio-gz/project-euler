##
# Problem 96
##
# Suduku solver

# Idea: Implement algorithm to solve each suduku.
from copy import deepcopy
from time import time
import numpy as np


class NoOptions(Exception):
    pass


def get_options(digits):
    """
    digits: A list of 9 digits from 0 to 9.
    Returns all digits between 1 and 9 that aren't
    part of digits.
    """
    result = []
    for n in range(1, 10):
        if n not in digits:
            result.append(n)
    return set(result)


def get_boxes(grid):
    """
    grid: A 9x9 grid.
    Returns array with arrays of 3x3 boxes of grid.
    """
    grid2 = np.split(grid, 3)
    boxes = np.hsplit(grid2[0], np.array([3, 6]))
    for i in range(1, 3):
        boxes.extend(np.hsplit(grid2[i], np.array([3, 6])))
    for index in range(9):
        boxes[index] = boxes[index].reshape(1, 9)[0]
    return np.array(boxes)


def box_indexes():
    """
    Returns a list of box indexes for each element of the
    9x9 grid.
    """
    indexes = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append((i//3)*3 + j//3)
        indexes.append(row) 
    return indexes


def get_all_options(grid):
    """
    grid: A 9x9 array.
    Will return a list of all possible digits free for each case.
    Assigns empty list for cases already filled.
    """
    def miss_by_rows(grid):
        result = []
        for row in grid:
            result.append(get_options(row))
        return result

    def miss_by_columns(grid):
        return miss_by_rows(grid.transpose())

    def miss_by_boxes(grid):
        return miss_by_rows(get_boxes(grid))

    options_row = miss_by_rows(grid)
    options_col = miss_by_columns(grid)
    options_box = miss_by_boxes(grid)
    indexes = box_indexes()
    options = []
    for i in range(9):
        row_options = []
        for j in range(9):
            box_index = indexes[i][j]
            if not grid[i][j]:
                row_options.append(list(options_row[i] & options_col[j] &
                                        options_box[box_index]))
            else:
                row_options.append([grid[i][j]])
        options.append(row_options)
    return options


def is_solution(grid):
    """
    Checks all rows/cols/boxes are different digits 1-9.
    Returns True for good solutions, False otherwise.
    """
    if np.all(np.sum(grid, axis=1) == 45) and \
       np.all(np.sum(grid, axis=0) == 45) and \
       np.all(np.sum(get_boxes(grid), axis=1) == 45):
        return True
    return False


def fill_single_options(grid, options=None, p=False):
    """
    grid: A 9x9 grid
    Iteratively fills all single options and
    returns the filled grid.
    """
    grid = grid.copy()
    if not options:
        options = get_all_options(grid)
    any_fill = True
    while any_fill:
        any_fill = False
        for i in range(9):
            for j in range(9):
                if len(options[i][j]) == 1 and grid[i][j] == 0:
                    if p:
                        print('Fill!')
                    grid[i][j] = options[i][j][0]
                    options = get_all_options(grid)
                    any_fill = True

    return grid


def correct_options(grid, options=None, min_options=2):
    """
    min_options: upper limit to test case options.
    Will attempt guessing to find impossible options.
    Returns the corrrected options grid.
    """
    def is_wrong(g, i1, i2):
        g = g.copy()
        g = fill_single_options(g)
        o = get_all_options(g)
        for i in range(9):
            for j in range(9):
                if len(o[i][j]) == 0:
                    #print('Wrong option!')
                    #print('Option: {} at {}, {}'.format(g[i1][i2], i1, i2))
                    return True
        return False
    if not options:
        options = get_all_options(g)
    if not min_options:
        min_options = 2
    corrections = False
    g = grid.copy()
    new_options = deepcopy(options)
    for min_options in range(2, min_options + 1):
        for i in range(9):
            for j in range(9):
                if len(options[i][j]) == min_options:
                    for option in options[i][j]:
                        if g[i][j] == 0:
                            g[i][j] = option
                            if is_wrong(g, i, j):
                                corrections = True
                                new_options[i][j].remove(option)
                            g[i][j] = 0

    if not corrections:
        raise NoOptions

    return new_options


def sudoku(grid):
    """
    grid: A 9x9 sudoku grid.
    Returns the solved grid.
    Returns None if can't solve.
    """
    grid = grid.copy()
    grid = fill_single_options(grid)
    if is_solution(grid):
        return grid
    options = get_all_options(grid)
    while True:
        try:
            options = correct_options(grid, options)
            grid = fill_single_options(grid, options)
            grid = fill_single_options(grid, options)
            if is_solution(grid):
                return grid
        except NoOptions:
            break
    while True:
        try:
            options = correct_options(grid, options, 9)
            grid = fill_single_options(grid, options)
            grid = fill_single_options(grid, options)
            if is_solution(grid):
                return grid
        except NoOptions:
            break
    for i in range(9):
        for j in range(9):
            if len(options[i][j]) == 2:
                for option in options[i][j]:
                    guess = grid.copy()
                    guess[i][j] = option
                    solution = sudoku(guess)
                    if solution is not None:
                        return solution
    #print('No solution')
    return None


grids = []
with open('p096_sudoku.txt') as file:
    line = file.readline()
    grid = ''
    while line:
        if line[0] == 'G':
            if grid:
                grids.append(np.array(list(map(int, grid))).reshape(9, 9))
                grid = ''
        else:
            grid += line[:9]
        line = file.readline()
    grids.append(np.array(list(map(int, grid))).reshape(9, 9))

start = time()
sums = 0
for index, grid in enumerate(grids):
    grid = sudoku(grid)
    grids[index] = grid
    sums += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
print('The answer is', sums)
print('Elpased: {}'.format(round(time() - start, 2)))
