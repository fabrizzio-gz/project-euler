"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10

In general, (nr)=n!r!(n−r)!
, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1

It is not until n=23
, that a value exceeds one-million: (2310)=1144066

How many, not necessarily distinct, values of (nr)
for 1≤n≤100, are greater than one-million?
"""
import math

def combinations(n, r):
    """
    n, r: Integers such that r <= r
    Returns n!/n!(n-r)! = n*(n-1)*...(n - r + 1)/r!
    """
    numerator = 1
    for operation in range(r):
        numerator *= n
        n -= 1
    return numerator/math.factorial(r)

val = 10**6
count = 0

for n in range(23, 101):
    greater = False
    for r in range(1, n):
        if combinations(n, r) > val:
            count += 1
            greater = True
        elif greater:
            # Combinations has started decreasing, pass to next n
            break
print(count)