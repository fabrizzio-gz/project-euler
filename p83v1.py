##
# Problem 83
##
# Get the minimal sum path by moving in all directions.

# Idea: Get shortest path to best lowest sum cell, starting from
# bottol right corner.
def get_minimal(m, ms, i_current, j_current):
    """
    m: matrix of values (nxn)
    ms: matrix of minimal sum path (0 if none)
    i_current, j_current: i,j indexes of current cell
    Updates ms[i_current][j_current] to the minimal path sum either
    by reaching the end (m[n-1][n-1]) or by reaching the cell in ms that yields
    a minimal sum.
    """
    n = len(m)
    current_cell_val = m[i_current][j_current]
    # Current cell is already minimal:
    if (i_current, j_current) == (n-1, n-1):
        ms[i_current][j_current] = current_cell_val
        return None
    # See if populating column or row:
    col_populate = False
    row_populate = False
    
    if i_current >= j_current:
        # Take min sum to the right
        next_min = ms[i_current][j_current + 1]
        col_populate = True
    else:
        # Take cell down
        next_min = ms[i_current + 1][j_current]
        row_populate = True
    # Reference minmal value
    minimal_sum = next_min + current_cell_val
    # Start checking rows with min sums, depending on row on column populate:
    # Also need to check moving left and up according to populate order
    if col_populate:
        # Check value below (if any)
        if i_current != n - 1:
            minimal_sum_ref = ms[i_current + 1][j_current] + current_cell_val
            if minimal_sum_ref < minimal_sum:
                minimal_sum = minimal_sum_ref
        # Check cells summing up and then to the right:
        row_up = i_current - 1
        sum_up = current_cell_val + m[row_up][j_current]
        while sum_up < minimal_sum and row_up > j_current:
            minimal_sum_right = ms[row_up][j_current + 1]
            if minimal_sum_right:
                minimal_sum_ref = sum_up + minimal_sum_right
                if minimal_sum_ref < minimal_sum:
                    minimal_sum = minimal_sum_ref
            row_up -= 1
            sum_up += m[row_up][j_current]
            
    if row_populate:
        # Check value to the right (if any)
        if j_current != n - 1:
            minimal_sum_ref = ms[i_current][j_current + 1] + current_cell_val
            if minimal_sum_ref < minimal_sum:
                minimal_sum = minimal_sum_ref
        # Check cells moving left and then down (while in domain of ms cells)
        col_left = j_current - 1
        sum_left = current_cell_val + m[i_current][col_left]
        while sum_left < minimal_sum and col_left >= i_current:
            minimal_sum_down = ms[i_current + 1][col_left]
            if minimal_sum_down:
                minimal_sum_ref = sum_left + minimal_sum_down
                if minimal_sum_ref < minimal_sum:
                    minimal_sum = minimal_sum_ref
            col_left -= 1
            sum_left += m[i_current][col_left]

    # Check cells by moving back one column then going down then going right
    # to reach ms values
    if col_populate and i_current < n - 2 and i_current > 0:
        j_left = j_current - 1
        sum_down = current_cell_val + m[i_current][j_left] + m[i_current + 1][j_left]
        for i_down in range(i_current + 2, n):
            sum_down += m[i_down][j_left]
            minimal_sum_ref = sum_down + ms[i_down][j_current]
            if minimal_sum_ref < minimal_sum:
                minimal_sum = minimal_sum_ref
            if sum_down > minimal_sum:
                break
    ## Check cells by moving up one row then moving to the right and then down
    if row_populate and j_current < n - 2 and j_current > 0:
        i_up = i_current - 1
        sum_right = current_cell_val + m[i_up][j_current] + m[i_up][j_current + 1]
        for j_right in range(j_current + 2, n):
            sum_right += m[i_up][j_right]
            minimal_sum_ref = sum_right + ms[i_current][j_right]
            if minimal_sum_ref < minimal_sum:
                minimal_sum = minimal_sum_ref
            if sum_right > minimal_sum:
                break
    # Special case for diagonal values (Also check by going up one row then going towards the right):
    if i_current == j_current and i_current > 0:
        i_up = i_current - 1
        sum_right = current_cell_val + m[i_up][j_current] + m[i_up][j_current + 1]
        for j_right in range(j_current + 2, n):
            sum_right += m[i_up][j_right]
            minimal_sum_ref = sum_right + ms[i_current][j_right]
            if minimal_sum_ref < minimal_sum:
                minimal_sum = minimal_sum_ref
            if sum_right > minimal_sum:
                break   
    # Check cells below with a detour: go back one column and start moving
    # down before turning right again to any ms_cell
    ms[i_current][j_current] = minimal_sum



# Matrix
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
#breakpoint()
# Matrix of minimal sums
#ms = [[0 for i in range(n)] for j in range(n)]
ms = [[None for i in range(n)] for j in range(n)]
# Populate minimal sum starting from left corner:
# d: distance from corner
for d in range(n):
    limit_index = n - d - 1
    # Populate column from bottom:
    for row in range(n - 1, limit_index, -1):
        get_minimal(m, ms, row, limit_index)
    # Populate row from right end:
    for col in range(n - 1, limit_index, -1):
       get_minimal(m, ms, limit_index, col)
    # Populate diagonal:
    get_minimal(m, ms, limit_index, limit_index)
print(ms[0][0])
