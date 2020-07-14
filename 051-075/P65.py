"""
What is most surprising is that the important mathematical constant,
e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...]

The first ten terms in the sequence of convergents for e are:

2,3,83,114,197,8732,10639,19371,1264465,1457536,...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e
"""
from fractions import Fraction

def get_euler_fraction(sequence):
    """
    sequence: A list of the continued fraction expression of the numerator.
    Returns the continued fraction produced by the sequence.
    """
    sub = 0
    for val in reversed(sequence):
        denom = val + sub
        sub = Fraction(1, denom)
    return Fraction(denom)

def get_euler_sequence(n):
    """
    Returns a list of the n first continued fractions of the euler continued fraction.
    """
    sequence = []
    # First 2 terms
    if n >= 1:
        sequence.append(2)
    if n >= 2:
        sequence.append(1)
    count = 1
    n -= 1
    for i in range(1, n):
        if i%3 == 1:
            sequence.append(count*2)
            count += 1
        else:
            sequence.append(1)
    return sequence

def sum_digits(num):
    """
    Returns the sums of the digits of int num
    """
    num_str = str(num)
    digits = [int(digit) for digit in num_str]
    return sum(digits)

n = 100
sequence = get_euler_sequence(n)
euler_fraction = get_euler_fraction(sequence)
print(euler_fraction)
print(sum_digits(euler_fraction.numerator))
