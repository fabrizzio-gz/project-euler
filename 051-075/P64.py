"""
√23=[4;(1,3,1,8)]
Exactly four continued fractions, for N≤13, have an odd period.

How many continued fractions for N≤10000 have an odd period?
"""
from math import sqrt

def print_fraction(x, a, b, num):
    """
    Prints the fraction with given  values.
    """
    print('{}, {} / sqrt({}) - {}'.format(a, num, x, b))

def get_cycles(x):
    """
    Gets each succesive approximation of sqrt(n) as continued fractions.
    """
    i = int(x**.5) # Closest perfect square
    d = x - i**2 # Denominator
    a = 2*i//d # First a
    b = i - 2*i%d # First sqrt(n) - b
    num = d # First numberator when inversing fraction
    #print_fraction(x, a, b, num) # Next inverse fraction is: num / (sqrt(x) - b)
    fraction_past = []
    fraction_past.append((num, b))
    period = 1
    while True:
        d = x - b**2
        # Update coefficients
        a, b, num = (b+i)*num // d, i - ((b+i)*num%d) // num, d // num
        # Check for repetition
        if (num, b) not in fraction_past:
            fraction_past.append((num, b))
            #print_fraction(x, a, b, num)
            period += 1
        else:
            break
    #print('Period of:', period)
    return period

perfect_squares = [n**2 for n in range(1,101)]
counter = 0
for x in range(2,10000 +1):
    # Check value is not a perfect square
    if x not in perfect_squares:
        period = get_cycles(x)
        if period % 2 == 1:
            counter += 1
print(counter)
