##
# Problem 82
##
# Finding minimal path sum from left to right
# Idea: Getting the minimal sum for each element on rightmost column
from operator import add

def get_minimal_sum(m, j, minimal_sums_next_col):
    """
    m: matrix of values (n x n)
    j: column to evaluate:
    minimal_sums: List of minimal sums for column j+1
    Returns a list of size n of minimal sums for each row.
    """
    n = len(m)
    # Start with value at current column
    current_column_values = []
    for i in range(n):
        current_column_values.append(m[i][j])
    if j == n - 1:
        # Already at right end
        return current_column_values
    # As a reference, take sum moving directly to the right
    minimal_sums = list(map(add, current_column_values, minimal_sums_next_col))
    for i in range(n):
        # Check values upwards:
        # Start for each row with current element
        sums_up = current_column_values[i]
        for i_up in range(i - 1, -1, -1):
            sums_up += current_column_values[i_up]
            if sums_up > minimal_sums[i]:
                break
            # See if it's good to move to the right at i_up
            move_right = sums_up + minimal_sums_next_col[i_up]
            if move_right < minimal_sums[i]:
                minimal_sums[i] = move_right
        # Check values down:
        # Start for each row with current element
        sums_down = current_column_values[i]
        for i_down in range(i+1, n):
            sums_down += current_column_values[i_down]
            if sums_down > minimal_sums[i]:
                break
            move_right = sums_down + minimal_sums_next_col[i_down]
            if move_right < minimal_sums[i]:
                minimal_sums[i] = move_right
    return minimal_sums
                
# Matrix of values:
with open('p082_matrix.txt', 'r') as f:  
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
minimal_sums = []
for j in range(n-1, -1, -1):
    minimal_sums = get_minimal_sum(m, j, minimal_sums)
print(min(minimal_sums))
