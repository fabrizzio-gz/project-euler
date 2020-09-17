import numpy as np


def get_unitary_vector(u):
    """
    u : a tuple of ints x, y
    Return the unitary vector u_hat: u/|u|
    """
    magnitude = get_magnitude(u)
    return (u[0] / magnitude, u[1] / magnitude)


def get_magnitude(u):
    """Return the magnitude of tuple u = (x, y)"""
    return (u[0] ** 2 + u[1] ** 2) ** .5


def solve(x, u, v):
    """
    x, u, v : tuples of 2 ints
    x : The origin
    u : The 1st direction
    v : The 2nd direction
    Calculates a, b such that (u v)(a b) = - x
    """
    # B
    x = np.array(x)
    
    u = np.array(u)
    u = u - x
    v = np.array(v)
    v = v - x

    # Matrix A
    u_ver = np.vstack(u)
    v_ver = np.vstack(v)
    mat = np.hstack((u_ver, v_ver))

    # See if origin is attained with: Ax + B = 0
    sol = np.linalg.inv(mat).dot(-x)
    a, b = sol

    # If solutions are less than magnitudes, True
    return 0 <= a <= 1 and 0 <= b <= 1 and \
        b <= 1 - a # To limit the area within a triangle

with open('p102_triangles.txt') as file:
    line = file.readline()
    triangles = []
    while line:
        line = line.strip().split(',')
        line = list(map(int, line))
        x = line[0], line[1]
        u = line[2], line[3]
        v = line[4], line[5]
        triangles.append((x, u, v))
        line = file.readline()
    #triangles.append((x, u, v))


# x = (-340, 495)
# u = (-153, -910)
# v = (835, -947)
# x = (-175, 41)
# u = (-421, -714)
# v = (574, -645)
#print(len(list(filter(solve, triangles))))

counter = 0
total = 0
for x, u, v in triangles:
    total += 1
    if solve(x, u, v):
        counter += 1

print(counter)
    
#solve(x, u, v)
