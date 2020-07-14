"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import itertools
from math import log10

def cubic_numbers(digits):
    """
    Returns a list of all perfect cubes of digits digits.
    """
    min_val = 10**(digits-1)
    max_val = min_val*10
    min_cube = int(min_val**(1/3)) + 1
    max_cube = int(max_val**(1/3))
    cubes = [val**3 for val in range(min_cube, max_cube + 1)]
    return cubes 

def get_iterations(cubes):
    """
    cubes: a list of numbers
    Returns a dictionary: digits -> #
    """
    # Convert cubes to str
    cubes_str = list(map(str, cubes))
    # Get a sorted list of digits for each cube
    cubes_digits = list(map(sorted, list(map(list, cubes_str))))
    cubes_digits = list(map(str.join, ['']*len(cubes), cubes_digits))
    cubes_dict = {}
    for key_cubes in cubes_digits:
        cubes_dict[key_cubes] = cubes_dict.get(key_cubes, 0) +1
    return cubes_dict

def max_key(cubes_dict):
    """
    cubes_dict: dictionary digits-> cubic permutations
    Returns the key with the max counts
    """
    max_count = 0
    key_max = ''
    for key in cubes_dict.keys():
        if cubes_dict[key] > max_count:
            max_count = cubes_dict[key]
            key_max = key
    return max_count, key_max

def get_cube(cubes, key):
    """
    cubes: A list of cubes
    key: An ordered list of the digits of cube
    Returns a list of cubes with the same key
    """
    # Convert cubes to str
    cubes_str = list(map(str, cubes))
    # Get a sorted list of digits for each cube
    cubes_digits = list(map(sorted, list(map(list, cubes_str))))
    cubes_digits = list(map(str.join, ['']*len(cubes), cubes_digits))
    index_search = 0
    for index, key_cube in enumerate(cubes_digits):
        if key_cube == key:
            index_search = index
            break
    return cubes[index_search]
    
digits = 2
target_count = 5
max_count = 0
key_max = ''
while max_count < target_count:
    max_count, key_max = max_key(get_iterations(cubic_numbers(digits)))
    digits += 1
cubes = cubic_numbers(digits - 1)
digits = key_max
print(get_cube(cubes, key_max))

## Amazing solution from project Euler

# from collections import Counter

# cubes_permuted = {i*i*i : (''.join(sorted(str(i*i*i)))) for i in range(10000)}
# cubes_count = Counter(cubes_permuted.values())
# result = list(cubes_count.keys())[list(cubes_count.values()).index(5)]

# print([i[0] for i in cubes_permuted.items() if i[1] == result])