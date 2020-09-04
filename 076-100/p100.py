##
# Problem 100
##

# Transforming the probability r*r-1 / t*t-1
# Into Pell's equation: x² - 2y² = 1
# With r = x + 1 / 2, t = 2 * y - 1
from math import sqrt


def expand_solutions(x, y):
    return (3*x + 4*y, 2*x + 3*y) 


def get_balls(x, y):
    return ((x+1)/2 , (y+1)/2)

x = 1
y = 1
t, r = 0, 0
while t < 10**12:
    x, y = expand_solutions(x, y)
    t, r = get_balls(x, y)
    print(t, r)
