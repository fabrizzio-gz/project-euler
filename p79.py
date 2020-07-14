##
# Problem 79
##
# Finding the minimum length of a code.
from itertools import permutations

def get_combinations(n):
    """
    Gets the possible 3-digit combinations for a code of 
    n digits. Digits in ascending order. n >= 3
    Returns a list of possible combinations.
    """
    combinations = []
    for digit1 in range(n - 2):
        for digit2 in range(digit1 + 1, n - 1):
            for digit3 in range(digit2 + 1, n):
                combinations.append([digit1, digit2, digit3])
    return combinations

def validate_code(code, digit_order, login):
    """
    code: A list with the current code digits (None for unkown digits)
    digit_order: Says to which code digit corresponds the login digits 
    login: A 3 digit number (str)
    Returns True if possible code attempts, False otherwise.
    Will update the unkown digits in code accordingly.
    """
    for index, digit in zip(digit_order, login):
        # Updates char in code
        if not code[index]:
            code[index] = digit
        # Verifies correspondance if code already has a digit at index
        elif not code[index] == digit:
            return False
    return True

def solve(logins):
    """
    logins: list of unique 3 digit logins
    return the shortest possible code to validate all logins
    """
    for n in range(3, 100):
        print('Checking', n, 'digits code.')
        code = [None] * n
        # Gets all possible combinations for n digits
        combinations = get_combinations(n)
        # Verify there are enough combinations for all logins:
        if len(combinations) < len(logins):
            continue
        # Check all possible combinations
        for combination_order in permutations(combinations):
            for digit_order, login in zip(combination_order, logins):
                if not validate_code(code, digit_order, login):
                    break 
            else:
                return code
    # Unable to get a code
    return False

# Get logins
with open('p079_keylog.txt', 'r') as f:  
    logins = f.read().splitlines()
# Unique logins
logins = list(set(logins))
#print('Possible logins: ', logins)

print(solve(logins))


