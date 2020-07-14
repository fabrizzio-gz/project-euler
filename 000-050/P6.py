"""
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the 
square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and 
the square of the sum.
"""
# How many numbers
n = 100

# Formula: 2 x [n x sum(n-1) + n-1 x sum (n-2) + ... 2 x 1]
vals = list(range(n, 0, -1))


sumterms = 0
for i in range(n - 1):
    sumterms += vals[i] * sum(vals[i + 1:])

sumterms *= 2 # Following the "formula"

print(sumterms)