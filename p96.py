##
# Problem 96
##
# Suduku solver

# Idea: Implement algorithm to solve each suduku.
from itertools import permutations
import numpy as np

def get_options(digits):
    """
    digits: A list of 9 digits from 0 to 9.
    Returrns all digits between 1 and 9 that aren't
    part of digits.
    """
    result = []
    for n in range(1, 10):
        if n not in digits:
            result.append(n)
    return set(result)


def get_column_options(column):
    """
    columns: An array of 9 digits (0 - 9)
    Returns a list of all digits 1-9 that are not part of
    'coolumn'
    """
    return get_options(column)


def get_row_options(line):
    """
    line: A list of 9 digits corresponding to a 
    sudoku line.
    Returns a list of the possible options, that is
    the digits 1 - 9 that are not present in 'line'.
    """
    return get_options(line)

def get_box_options(box):
    """
    box: An array of 9 digits (0-9)
    Returns a list of all digits (1-9) that aren't part
    of 'box'
    """
    return get_options(box)


def miss_by_rows(grid):
    """
    grid: A 9x9 array
    Returns a list of lists. One for each row, with
    the digits not part of the row.
    """
    result = []
    for row in grid:
        result.append(get_row_options(row))
    return result


def miss_by_columns(grid):
    return miss_by_rows(grid.transpose())


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


def get_indexes():
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


def miss_by_boxes(grid):
    return miss_by_rows(get_boxes(grid))


def get_all_options(grid):
    """
    grid: A 9x9 array.
    Will return a list of all possible elements for each element.
    """
    options_row = miss_by_rows(grid)
    options_col = miss_by_columns(grid)
    options_box = miss_by_boxes(grid)
    indexes = get_indexes()
    options = []
    for i in range(9):
        row_options = []
        for j in range(9):
            box_index = indexes[i][j]
            row_options.append(list(options_row[i] & options_col[j] \
                               & options_box[box_index]))
        options.append(row_options)
    return options


def is_solved(grid):
    """
    Checks if there's any 0 in grid
    """
    return np.sum(grid == 0) == 0


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
    array[array == 0] = np.array(values)


def solve(grid):
    """
    Iterative solution of 9x9 grid by filling
    cases that have only one possible option.
    """
    fills = True
    while fills:
        fills = False
        options = get_all_options(grid)
        for i in range(9):
            for j in range(9):
                if len(options[i][j]) == 1 and not grid[i][j]:
                    grid[i][j] = options[i][j][0]
                    fills = True
        if is_solution(grid):
            return grid
    # No more cases left to fill
    return None


def sudoku(grid):
    """
    Will solve the 9x9 grid. Filling zeros with 1-9 digits.
    Returns the solved sudoku if successful.
    Returns None object otherwise.
    """
    # Attempt simple iterative solution first
    solution = solve(grid.copy())
    if solution is not None:
        return solution
    # If no solution is found, randomly fill the row/col wit less zeros
    # and try to solve then.
 #   breakpoint()
    grid_copy = grid.copy()
    row = ''
    col = ''
    max_row = np.amax(np.sum(grid > 0, axis=1))
    if max_row != 9:
        row = np.argmax(np.sum(grid > 0, axis=1))
    max_col = np.amax(np.sum(grid > 0, axis=0))
    if max_col != 9:
        col = np.argmax(np.sum(grid > 0, axis=0))
    if row:
        #print('Solution through row', row)
        for row_options in permutations(get_row_options(grid_copy[row])):
            random_fill(grid_copy[row], row_options)
            solution = sudoku(grid_copy.copy())
            if solution is not None and is_solution(solution):
                #print(grid_copy)
                return solution
            else:
                grid_copy = grid.copy()
#    breakpoint()
    if col:
        #print('Solution via col', col)
        for col_options in permutations(get_column_options(grid_copy[:, col])):
            random_fill(grid_copy[:, col], col_options)
            solution = sudoku(grid_copy.copy())
            if solution is not None and is_solution(solution):
                #print(grid_copy)
                return solution
            else:
                grid_copy = grid.copy()
    return None


def get_min(grid, options = None):
    """
    Returns the minimum length item of options.
    """
    if not options:
        options = get_all_options(grid)
    min_len = 10
    for i in range(9):
        for j in range(9):
            if len(options[i][j]) < min_len and not grid[i][j]:
                min_len = len(options[i][j])
    return min_len


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

problems = 0
for index, grid in enumerate(grids):
    print(index)
    solution = sudoku(grid.copy())
    if solution is not None:
        grids[index] = solution
    else:
        print('Problem with grid {}'.format(index))
        problems +=1
print(problems)
