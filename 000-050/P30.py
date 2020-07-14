"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of 
their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def sum_5_digits(number):
    """
    number is any positive integer
    Returns the sum of the fifth power of its digits.
    """
    assert type(number) == int, "Not a valid input"
    str_number = str(number)
    sum_powers = 0
    for char in str_number:
        sum_powers += int(char)**5
    return sum_powers

number = 10
fifth_powers = []
while number < 360000:
    if sum_5_digits(number) == number:
        fifth_powers.append(number)
    number += 1
print(fifth_powers)