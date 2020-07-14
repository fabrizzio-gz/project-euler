"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of 
a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import prime as prime_mod

def is_composite(n, primes):
    """
    n is any odd number
    primes is a list of all primes < n
    Return True if the n can be written as an odd composite. False otherwise.
    """
    for prime in primes:
        if prime > n:
            return False
        square = ((n - prime)//2)**.5
        if square - int(square) < 10**-4:
            return True
    return False

limit = 10**6
primes = prime_mod.list_primes(limit)
print('here')
for n in range(3, limit + 1, 2):
    if not is_composite(n, primes):
        print(n)


