##
# Problem 83
##
# Get the minimal sum path by moving in all directions.

# Idea: Greedy algorithm: Move to next minimal value cell.
def next(m, pos, past_cells, cumulative_sum):
    """
    m: matrix of values (n x n)
    pos: (i, j) tuple of current (row, column)
    past_cells: list with past (i,j) indexes of cells already visited
    cumulative_sum: current cumulative_sum
    Returns indexes of next cell with minimal value and updated cumulative_sum:
    (i_next, j_next), new_cumulative_sum
    """
#    breakpoint()
    n = len(m)
    i, j = pos
    up = (i-1, j)
    down = (i+1, j)
    left = (i, j-1)
    right = (i, j+1)
    possible_steps = []
    for i_step, j_step in [up, down, left, right]:
        if (i_step, j_step) not in past_cells:
            if i_step >= 0 and j_step >= 0 and i_step<n and j_step<n:
                possible_steps.append((i_step,j_step))
    min_cell = None
    next_step = None
    for step_i, step_j in possible_steps:
        step_cell = m[step_i][step_j]
        if not min_cell:
            min_cell = step_cell
            next_step = (step_i, step_j)
        elif step_cell < min_cell:
            min_cell = step_cell
            next_step = (step_i, step_j)
    cumulative_sum += min_cell
    print(cumulative_sum, next_step)
    past_cells.append(next_step)
    return next_step, cumulative_sum

# Matrix of values:
with open('p083_matrix.txt', 'r') as f:  
    lines_raw = f.read().splitlines()
m = []
for line in lines_raw:
    char_line = line.split(',')
    m.append([int(string) for string in char_line])
# m = [[131, 673, 234, 103, 18],
#      [201, 96, 342, 965, 150],
#      [630, 803, 746, 422, 111],
#      [537, 699, 497, 121, 956],
#      [805, 732, 524, 37, 331]]
n = len(m)
pos = (0, 0)
cumulative_sum = m[0][0]
past_cells = [(0, 0)]
# Debug:
past_cells.append((0, 4))
while pos != (n-1, n-1):
    next_pos, cumulative_sum = next(m, pos, past_cells, cumulative_sum)
    pos = next_pos
print(cumulative_sum)
# Doesn't work. It gets stuck...
