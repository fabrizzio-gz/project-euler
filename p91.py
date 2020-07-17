##
# Problem 91 (v2)
##
# Finding right triangles inside a nxn (n = 50) grid.

# Idea: Combinatory and brute force.

def vertical_horizontal_sols(n):
    """
    n: grid size.
    Return al solutions with a vertical/horizontal hypotenuse.
    (Will not count solutions with equal length catheti)
    """
    sols = 0
    for hyp in range(2, n + 1):
        for y in range(1, hyp):
            for x in range(1, n + 1):
                # Right triangle condition
                if x**2 + y**2 == y*hyp:
                    if x != y:
                        #print(hyp, x, y)
                        sols += 1
    # Accounting for symmetry (horizontal hypotenuse)
    return 2 * sols


def diagonal_sols(n):
    """
    n: grid size.
    Returns all possible solutions with diagonal hypothenuse, catheti.
    """
    sols = 0
    for x1 in range(2, n + 1):
        for y1 in range(1, n + 1):
            c1 = x1**2 + y1 **2
            for x2 in range(1, x1):
                for y2 in range(y1 + 1, n + 1):
                    # Right triangle condition
                    if c1 == x1*x2 + y1*y2:
                        # print(x2, y2, x1, y1)
                        sols += 1
    # Consider symmetric solutions (inverting x and y)
    return 2*sols


def diagonal_sols_cw(n):
    """
    n: grid size.
    Returns all possible solutions with diagonal hypothenuse, catheti.
    Variant with hypothenuse clockwise relative to origin cathetus (x1,y1).
    """
    sols = 0
    # Counting solutions with cathetus1 below diagonal: x1 > y1
    for x1 in range(2, n + 1):
        for y1 in range(2, x1 + 1):
            c1 = x1**2 + y1 **2
            for x2 in range(x1 + 1, n + 1):
                for y2 in range(1, y1):
                    # Right triangle condition
                    if c1 == x1*x2 + y1*y2:
                        # print(x2, y2, x1, y1)
                        sols += 1
    # Consider symmetric solutions (inverting x and y)
    return 2*sols  
    

n = 50
# Solutions due to horizontal vertical catheti
sols = 3*n**2
# Triangles with one side along the diagonal
# (one possible solution every even length)
sols += n//2 * 2
sols += vertical_horizontal_sols(n)
sols += diagonal_sols(n)
print(sols)
