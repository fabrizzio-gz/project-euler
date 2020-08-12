##
# Problem 96
##
# Suduku solver

# Idea: Implement algorithm to solve each suduku.
# from itertools import permutations
from copy import deepcopy
import numpy as np

class NoOptions(Exception):
    pass


class NoSolution(Exception):
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
                row_options.append(list(options_row[i] & options_col[j] \
                               & options_box[box_index]))
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


def random_fill(array, values):
    """
    array: An array of 9 digits linked to a grid.
    values: tuple of digits 1-9
    Fills the zeros in array with 'values' in the
    order they appear.
    """
    array = array.copy()
    array[array == 0] = np.array(values)
    return array


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
#        options = get_all_options(grid)

    return grid


def correct_options(grid, min_options=2):
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
    if not min_options:
        min_options = 2
    corrections = False
    g = grid.copy()
    options = get_all_options(g)
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
        # print('No corrections')
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
            options = correct_options(grid)
            grid = fill_single_options(grid, options)
#            grid = fill_single_options(grid, options)
            if is_solution(grid):
                return grid
        except NoOptions:
            break
    while True:
        try:
            options = correct_options(grid, 9)
            grid = fill_single_options(grid, options)
#            grid = fill_single_options(grid, options)
            if is_solution(grid):
                return grid
        except NoOptions:
            break
    print('No solution')
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

# p96-grids5
# grid5 = grids[5]
# grid5 = fill_single_options(grid5)
# g = grid5.copy()
# o = get_all_options(g)
#sudoku(g)

def pp(options):
    for row in options:
        print(row)

problems = 0
loops = [9, 13, 25, 28, 43, 45, 46, 48]
for index, grid in enumerate(grids):
    if index not in loops:
        print(index)
        solution = sudoku(grid)
        if solution is not None:
            grids[index] = solution
        else:
            print('Problem with grid {}'.format(index))
            problems +=1
print('Problems with {} sudokus'.format(problems))
