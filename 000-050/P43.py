"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

def divisibility(number):
    """
    'number' is a string corresponding to a number
    Returns True if divisibility conditions are met.
    """
    def divisor_gen():
        divisors = [2, 3, 5, 7, 11, 13, 17]
        for divisor in divisors:
            yield divisor
    divisor = divisor_gen()
    for slice_index in range(1 , 8):
        number_slice = number[slice_index:slice_index+3]
        number_slice = int(number_slice)
        if not number_slice % next(divisor) == 0:
            return False
    return True

digits = '0123456789'
numbers = list(itertools.permutations(digits, 10))
numbers = list(map(str.join, ['']*len(numbers), numbers))
numbers = [number for number in numbers if number[0] != '0']
sum_numbers = 0
for number in numbers:
    if divisibility(number):
        sum_numbers += int(number)
print(sum_numbers)
