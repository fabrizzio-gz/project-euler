##
# Problem 87
##
# Get number of possible square, cube and fourth power combinations
# of primes.

# Idea: combination calculations.
import prime as prime_mod
from time import time

def get_powers(primes, goal, power_of):
    """
    primes: a list of all possible primes.
    goal: the limit value
    Returns a list of all powers of prime in primes that could
    produce a combination.
    Condition: prime power + minimum other addends are less than goal.
    """
    if power_of == 2:
        addends = 2**3 + 2**4
    elif power_of == 3:
        addends = 2**2 + 2**4
    elif power_of == 4:
        addends = 2**2 + 2**3
    else:
        raise ValueError('Power not valid', power_of)
    powers = []
    for prime in primes:
        power = prime**power_of
        if power + addends < goal:
            powers.append(power)
    return powers

def get_squares(primes, goal):
    """
    primes: a list of all possible primes.
    Returns a list of all squares that could produce a combination.
    Condition: prime**2 < goal - 2**3 - 2**4
    """
    return get_powers(primes, goal, 2)

def get_cubes(primes, goal):
    return get_powers(primes, goal, 3)
    
def get_fourths(primes, goal):
    return get_powers(primes,goal, 4)

goal = 50*10**6
primes = prime_mod.list_primes(int(goal**.5))
squares = get_squares(primes, goal)
cubes = get_cubes(primes, goal)
fourths = get_fourths(primes, goal)
count = 0
sums = []
start = time()
for square in squares:
    for cube in cubes:
        for fourth in fourths:
            sum_ = square + cube + fourth
            if sum_ < goal:
                if sum_ not in sums:
                    count += 1
                    sums.append(sum_)
end = time()
print(count, round(end - start, 2))
#breakpoint()
#count_combinations(9, cubes, fourths, goal)
