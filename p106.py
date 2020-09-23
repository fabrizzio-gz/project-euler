from p103 import get_groups

VARIABLES = '0abcdefghijklmnopqrstuvwxyz'


def delete_first_variable(equation_expression):
    return equation_expression.replace('0', '')


def get_number_variables(equation_expression):
    return len(equation_expression)


def variables_available(equation_expression):
    if not equation_expression:
        return False

    for var in VARIABLES:
        if var in equation_expression:
            return True
    return False


def is_side_zero(equation_expression):
    """An empty string is represented as 0"""
    return not bool(equation_expression)


def no_extras(equation_expression):
    """ `+` is a placeholder for 'extra variables'"""
    return equation_expression.replace('+', '0')

def delete_greatest_variable(left_side, right_side):

    greatest_common_var = min(max(no_extras(left_side)),
                              max(no_extras(right_side)))

    if greatest_common_var == '0':
        return left_side, right_side

    greatest_var_left = max(no_extras(left_side))
    greatest_var_right = max(no_extras(right_side))

    replacement = greatest_common_var + '+'
    if greatest_var_left > greatest_var_right:
        left_side = left_side.replace(greatest_var_left, replacement)
    elif greatest_var_left < greatest_var_right:
        right_side = right_side.replace(greatest_var_right, replacement)

    new_left_side = left_side.replace(greatest_common_var, '')
    new_right_side = right_side.replace(greatest_common_var, '')

    return new_left_side, new_right_side


def need_verify_equality(left_side, right_side):
    """
    Given ordered variables 0 - x.
    Verifies if equality between `left_side` and `right_side`
    is possible.
    It will return false if any of the sides left_side, right_side is left without
    variables.
    Each variable is represented with a number from 0 to x.
    """
#    breakpoint()
    # First variable is irrelevant for analysis and can be ommitted
    left_side = delete_first_variable(left_side)
    right_side = delete_first_variable(right_side)
    
    len_left = get_number_variables(left_side)
    len_right = get_number_variables(right_side)

    # Swap sides. Shortest side to the left
    if len_left > len_right:
        left_side, right_side = right_side, left_side

    while variables_available(left_side):
        left_side, right_side = delete_greatest_variable(left_side, right_side)

    return not (is_side_zero(left_side) or is_side_zero(right_side))


def get_string_groups(variables, group_size):
    for group in get_groups(variables, group_size):
        string1 = ''.join(sorted(group[0]))
        string2 = ''.join(sorted(group[1]))
        yield string1, string2


def get_equality_checks(size):
    variables = VARIABLES[:size]

    counter = 0
    for group_size in range(2, size//2 + 1):
        for left_side, right_side in get_string_groups(variables, group_size):
            if need_verify_equality(left_side, right_side):
                counter += 1

    return counter

## Solution:
# get_equality_checks(12)
