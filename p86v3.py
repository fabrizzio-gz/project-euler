##
# Problem 86
##
# Shortest cuboid path.

# Idea: Get the perfect cubics with iteration (brute force).
# The minimum distance is calculated by "folding" the 2 sides of the cube and
# getting the pytagoric distance.
# v3: Use of a generator for incremential results

# The cuboid will be length m1xm2xm3
from time import time
def get_perfect_squares(size=10000):
    """
    size: The maximum side size of the cuboid.
    Returns a list true, False values for the perfect squares between 1**2 and (size**2 + (2*size)**2, the maximum possible cuboid distance)
    """
    max_val = int(5**.5 * size)
    squares = [False for i in range((max_val + 1)**2)]
    square_nums = [val**2 for val in range(1, max_val + 1)]
    for square_num in square_nums:
        squares[square_num] = True
    return squares

def get_cuboids():
    """
    Gets the cuboids of size MxMxM with integer minimum path solutions.
    Each iteration yields count for M + 1
    """
    perfect_squares = get_perfect_squares()
    count = 0
    m1 = 0
    while True:
        m1 += 1
        for m2 in range(1, m1 + 1):
            for m3 in range(1, m2 + 1):
                l = m1**2 + (m2 + m3)**2
                if perfect_squares[l]:
                    count += 1
        yield m1, count

goal = 10**6
solution = get_cuboids()
start = time()
size, solutions = next(solution)
while solutions < goal:
    size, solutions = next(solution)
end = time()
print(size, solutions, round(end - start,2))
