"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# Brute force algorithm
sumdig = 1000

for a in range(1, sumdig - 1): 
    for n in range(1, sumdig - 1 - a):
        b = a + n
        c = sumdig - a - b
        a2b2 = a**2 + b**2
        c2 = c**2
        if a2b2 == c2:
            print('Success! Valuares are {}, {}, {}.'.format(a, b, c))
            print('Product:', a*b*c)
