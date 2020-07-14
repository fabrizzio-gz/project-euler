"""
    φ ( n ) = n ∏ p ∣ n ( 1 − 1 p )
"""
from prime import is_prime
from fractions import Fraction

# Using n/phi = ∏ ( 1 − 1 / p ) (were p is a prime divisor of n)

N = 1000000
max_ratio = 1
max_n = 0
primes = list(map(is_prime, range(0, N + 1)))

for n in range(2, N + 1):
    ratio = 1
    for p in range(2, n + 1):
        # Check if number is prime
        if primes[p] and n % p == 0:
            # n/phi_n
            ratio *= 1/(1 - 1/p)
    if ratio > max_ratio:
        max_ratio, max_n = ratio, n
        print(ratio, n)
print(max_n)