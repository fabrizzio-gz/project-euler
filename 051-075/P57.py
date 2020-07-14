"""
The next three expansions are 9970, 239169, and 577408, but the eighth expansion, 1393985

, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""
from math import log10
a = 3
b = 2
# iteration = a/b
count = 0
for iteration in range(1000):
    # Update iteration
    (a, b) = (a + 2*b, a + b)
    # Compare number of digits
    if int(log10(a)) > int(log10(b)):
        count +=1
print(count)