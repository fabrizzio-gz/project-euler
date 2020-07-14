###
# Problem 81
###
# Getting the sum of the first 100 decimal digits of
# the irratinal square roots of numbers less than 100.
from decimal import *
# Setting limit to 101 digits (to avoid rounding errors)
getcontext().prec = 120
decimal_sum = 0
square_nums = [x**2 for x in range(1,11)]

for n in range(1,100):
    if n not in square_nums:
        digits = str(Decimal(n).sqrt())
        # Delete decimal point
        digits = digits[0] + digits[2:]
        for index in range(100):
            decimal_sum += int(digits[index])
    else:
        print(n)
print(decimal_sum)