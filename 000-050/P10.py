"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(n):
    # No possible divisor beyond sqrt(n). Only odd divisors
    prime = True
    for div in range(3, int(n**.5) + 1, 2):
        if n % div == 0:
            prime = False
            return prime
    return prime

count = 2 * 10**6
# 2 prime number will be added last
number = 3
sumprime = 0

while number <= count:
    if is_prime(number):
        sumprime += number
    # Only odd numbers can be primes beyond 2
    number += 2

# Adding prime number 2
sumprime += 2
print('The sum of primes below', count, 'elevates to', sumprime)