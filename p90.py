##
# Problem 90
##
# Get number of combinations to write all square numbers
# with 2 6-digit dice.

# Idea: Check all combinations.
from itertools import combinations as comb


def check(die1, die2):
    """
    die_1, die_2: tuples of 6 numbers.
    Returns true if they can create all square numbers
    """
    def check_square(square, die1, die2):
        digit1 = square // 10
        digit2 = square % 10
        cond2 = False
        if digit2 == 6:
            cond2 = (digit1 in die1 and 9 in die2) or \
                    (9 in die1 and digit1 in die2)
        cond1 = (digit1 in die1 and digit2 in die2) or \
                (digit2 in die1 and digit1 in die2)
        return cond1 or cond2
    # Changing all 9s with 6s and changing order of digits so that
    # 6 only occurs in units place.
    squares = [1, 4, 6, 16, 25, 36, 46, 81]
    for square in squares:
        if not check_square(square, die1, die2):
            return False
    return True


combinations = comb(range(10), 6)
count = 0
for die_1 in combinations:
    for die_2 in combinations:
        if check(die_1, die_2):
            count += 1
print(count)
