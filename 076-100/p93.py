##
# Problem 93
##
# Combination of arithmetic operations between 4 digits.

# Idea: Check all combinations.
from itertools import permutations


def create_parens(pos, val):
    parens_blank = [' '] * 6
    for pos_x, val_x in zip(pos, val):
        parens_blank[pos_x] = val_x
    return parens_blank


def initialize_parens():
    """
    Initializes all possible parens combinations.
    """
    parens_combinations = list()

    # Adding 10 possible parens combinations
    parens_combinations.append(create_parens([0, 2, 3, 5], ['(', ')', '(', ')']))
    parens_combinations.append(create_parens([0, 2], ['(', ')']))
    parens_combinations.append(create_parens([3, 5], ['(', ')']))
    parens_combinations.append(create_parens([1, 4], ['(', ')']))
    parens_combinations.append(create_parens([0, 4], ['(', ')']))
    parens_combinations.append(create_parens([1, 5], ['(', ')']))
    parens_combinations.append(create_parens([0, 2, 4], ['((', ')', ')']))
    parens_combinations.append(create_parens([1, 4, 5], ['((', ')', ')']))
    parens_combinations.append(create_parens([1, 3, 5], ['(', '(', '))']))
    parens_combinations.append(create_parens([0, 1, 4], ['(', '(', '))']))
    
    return parens_combinations


def create_string(parens, digits, ops):
    str_ = parens[0] + digits[0] + ops[0] + \
           parens[1] + digits[1] + parens[2] + ops[1] + \
           parens[3] + digits[2] + parens[4] + ops[2] + \
           digits[3] + parens[5]
    return str_


def get_max(results):
    n = 1
    while True:
        if n not in results:
            return n - 1
        n += 1


def round_special(n):
    if abs(n - int(n)) > .01:
        return 0
    else:
        return round(n)

        
digit_permutations = permutations(range(1,10), 4)
digit_permutations = [perm for perm in digit_permutations if sorted(perm) == list(perm)]
ops = ['+', '-', '*', '/']
op_combinations = [(op1, op2, op3) for op1 in ops for op2 in ops
                   for op3 in ops]
parens_combinations = initialize_parens()

max_ = 0
max_digits = '1234'
for digits_int in digit_permutations:
    results = set()
    digits_str = list(map(str, digits_int))
    for digits in permutations(digits_str):
        for ops in op_combinations:
            for parens in parens_combinations:
                str_ = create_string(parens, digits, ops)
                try:
                    results.add(round_special(eval(str_)))
                except ZeroDivisionError:
                    pass
    new_max = get_max(results)
    print(new_max, digits_str)
    if new_max > max_:
        max_ = new_max
        max_digits = ''.join(digits_str)
print(max_, max_digits)
