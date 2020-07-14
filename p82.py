###
# Problem 82
##
# Find the lowest sum from one end to the other end.

### Debug column indexes...

def lowest_couple(m, j):
    """
    m: matrix of values (n x n)
    j: left column index (0, n-2)
    Returns i, m[i][j] and m[i][j+1] that sum = m[i][j] + m[i][j+1] is minimum.
    """
    min_sum = m[0][j] + m[0][j+1]
    min_i = 0
    for i in range(1, len(m)):
        sum_row = m[i][j] + m[i][j+1]
        if sum_row < min_sum:
            min_sum = sum_row
            min_i = i
    return min_i, m[min_i][j], m[min_i][j+1]

def get_deviation(m, i_start, j):
    """
    m: matrix of values (n x n)
    i_start: current row
    j: column index to evaluate (current column j  - 1)
    Returns i_deviation, addend_deviation such that:
    Addition of values vertically from i_start (not included) to i_deviation
    plus m[i_deviation][j] is a minimum (values along minimum sum path).
    """
#    breakpoint()
    i_deviation = i_start
    j_left = j 
    j_right = j + 1
    # Reference: move straigh to the left:
    min_addend = m[i_start][j_left]
    # Scanning values down:
    vertical_sum_downwards = 0 
    for i_down in range(i_start+1, n):
        vertical_sum_downwards += m[i_down][j_right]
        # Check moving to the left at i_down
        addend_down = vertical_sum_downwards + m[i_down][j_left]
        if addend_down < min_addend:
            min_addend = addend_down
            i_deviation = i_down
        elif addend_down > min_addend:
            break
    # Scan values upwards
    vertical_sum_upwards = 0
    for i_up in range(i_start-1,-1,-1):
        vertical_sum_upwards += m[i_up][j_right]
        # Check moving to the left at i_down
        addend_up = vertical_sum_downwards + m[i_up][j_left]
        if addend_up < min_addend:
            min_addend = addend_up
            i_deviation = i_up
        elif addend_down > min_addend:
            break
    return i_deviation, min_addend
        
# Matrix of values:
m = [[131, 673, 234, 103, 18],
     [201, 96, 342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37, 331]]
n = len(m)
# Start with lowest possible couple from right end
i_start, left_val, right_val = lowest_couple(m, n - 2)
min_sum = left_val + right_val
#breakpoint()
# Scans next columns from right to left
for j_left in range(n-3, -1, -1):
    i_next, left_val, right_val = lowest_couple(m, j_left)
    # Continue straight on if on the same row:
    if i_next == i_start:
        min_sum += left_val
        continue
    # Gets best path from i_start
    print('Deviation at', j_left)
    i_deviation, addend_deviation = get_deviation(m, i_start, j_left)
    deviation_sum = min_sum + addend_deviation
    # See if i_next is parth of the deviation:
    if i_next == i_deviation:
        i_start = i_deviation
        min_sum = deviation_sum
    # Still needs to check alternative path from i_start if not part of the deviation
print(min_sum)
    

