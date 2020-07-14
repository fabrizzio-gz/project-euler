"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the 
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , n) where n > 1?
"""

def con_product(n, vals):
    """
    n: an integer
    vals: a list of digits 1, 2,... up  9
    Returns string: the concatenated product of n and each digit in vals
    """
    products = list(map(lambda x: str(x * n), vals))
    return ''.join(products)

def is_pandigital(string):
    """
    Returns true if string includes all digits 1 to 9 and no more.
    """
    if '0' in string:
        return False
    if len(string) != 9:
        return False
    if len(set(string)) != 9:
        return False
    return True

max_pandigital = 0
# Starts generating list of multipliers starting from 9 digits, to a minimum of 2 multipliers
for multiplier_max in range (9, 1, -1):
    # Generates a list of multipliers from 1 to multiplier max
    multiplier_list = list(range(1,multiplier_max + 1))
    multiplicand = 1
    concatenated_product = con_product(multiplicand, multiplier_list)
    while len(concatenated_product) <= 9:
        if is_pandigital(concatenated_product):
            if int(concatenated_product) > max_pandigital:
                max_pandigital = int(concatenated_product)
        multiplicand += 1
        concatenated_product = con_product(multiplicand, multiplier_list)
print(max_pandigital)
