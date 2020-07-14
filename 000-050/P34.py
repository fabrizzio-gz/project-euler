"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

def sum_factorial_digits(number):
    """
    number is any int > 0.
    Returns the sum of the factorial of its digits
    """
    number_str = str(number)
    return sum([math.factorial(int(digit)) for digit in number_str])

max_num = math.factorial(9) * 7 
min_num = 3
factorial_number = []
for number in range(min_num, max_num + 7):
    if sum_factorial_digits(number) == number:
        factorial_number.append(number)

print(factorial_number)
print(sum(factorial_number))