"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math

number = 100
factorial = math.factorial(number)
fact_str = str(factorial)

sum_digs = 0
for digit in fact_str:
    sum_digs += int(digit)

print(sum_digs)

print(sum([int(digit) for digit in str(math.factorial(100))]))