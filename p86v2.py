##
# Problem 86
##
# Shortest cuboid path.

# Idea: Get the perfect cubics with iteration (brute force).
# The minimum distance is calculated by "folding" the 2 sides of the cube and
# getting the pytagoric distance.

# The cuboid will be length m1xm2xm3
def get_perfect_squares(size):
    """
    size: The maximum side size of the cuboid.
    Returns a list true, False values for the perfect squares between 1**2 and (size**2 + (2*size)**2, the maximum possible cuboid distance)
    """
    max_val = int(5**.5 * size)
    squares = [val**2 for val in range(1, max_val + 1)]
    return squares

size = 500
perfect_squares = get_perfect_squares(size)
count = 0
count_cuboids = 0

for m1 in range(1, size + 1):
    for m2 in range(1, m1 + 1):
        for m3 in range(1, m2 + 1):
            count_cuboids += 1
            l = m1**2 + (m2 + m3)**2
            if l in perfect_squares:
                count += 1
                #print(m1, m2, m3)
print(count, count_cuboids)
