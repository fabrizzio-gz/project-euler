##
# Problem 85
##
# Finding the number of rectangles contained inside a n x m grid.

# Idea: start with height = 1. Increase length from 1 to n.
# For each case, count the rectangles contained in the grid for a
# height = 1. Then proceed doing the same for height = 2, up to
# height = m.


def rectangles_contained(n, m):
    """
    n, m: dimensions of grid.
    Returns the number of rectangles contained.
    """
    return n*m*(n+1)*(m+1)//4

def get_difference(v1, v2):
    return abs(v1-v2)

def get_other_side(m, goal):
    """
    m: One length of the grid.
    goal: the desired number of grids.
    Returns the closest value to get a number of rectangles
    close to goal.
    """
    # Approximation by solving the rectangles_contained formula
    c = 4*goal/(m**2 + m)
    approx = ((4*c + 1)**.5 -1)/2
    return int(approx)

goal = 2*10**6
min_diff = goal
best_n = 0
best_m = 0
# Limit of 55 obtained by taking a square grid: n = m
for m in range(1, 55):
    n = get_other_side(m, goal)
    rec = rectangles_contained(n, m)
    diff = get_difference(rec, goal)
    if diff < min_diff:
        min_diff = diff
        best_n = n
        best_m = m
    # Get other closest value
    n += 1
    rec = rectangles_contained(n, m)
    diff = get_difference(rec, goal)
    if diff < min_diff:
        min_diff = diff
        best_n = n
        best_m = m
print(best_n, best_m)
