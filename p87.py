##
# Problem 87
##
# Get number of possible square, cube and fourth power combinations
# of primes.

# Idea: combination calculations.
import prime as prime_mod

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

def count_combinations(square, cubes, fourths, goal):
    """
    square: the square value.
    cubes: a list of possible cubes.
    fourths: a list of possible powers of 4.
    goal: maximum sum value
    Returns the number of possible sums.
    """
    last_cube_index = len(cubes) - 1
    last_fourth_index = len(fourths) - 1
    cube = cubes[last_cube_index]
    fourth = fourths[last_fourth_index]
    while square + cube + fourth >= goal:
        # Check if out of bounds:
        if last_cube_index < 0 or last_fourth_index < 0:
            return 0
        # Get next lowest value:
        if last_cube_index == 0:
            next_cube = cube
        else:
            next_cube = cubes[last_cube_index - 1]
        if last_fourth_index == 0:
            next_fourth = fourth
        else:
            next_fourth = fourths[last_fourth_index - 1]
        # Choose the next greatest value to compare
        if next_cube > next_fourth:
            cube = next_cube
            last_cube_index -= 1
        else:
            # If it's the last fourth, reduce cube instead
            if last_fourth_index == 0:
                cube = next_cube
                last_cube_index -= 1
            else:
                fourth = next_fourth
                last_fourth_index -= 1
        
    return (last_cube_index + 1) * (last_fourth_index + 1)

goal = 100
primes = prime_mod.list_primes(int(goal**.5))
squares = get_squares(primes, goal)
cubes = get_cubes(primes, goal)
fourths = get_fourths(primes, goal)
count = 0
for square in squares:
    count += count_combinations(square, cubes, fourths, goal)
print(count)
#breakpoint()
#count_combinations(9, cubes, fourths, goal)
