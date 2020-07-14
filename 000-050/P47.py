"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""
import prime as prime_mod

def get_factors(n):
    """
    n: any integer >= 2
    primes: list of primes.
    Returns a list of number n decomposed in its prime factors.
    """
    global primes
    n_init = n
    factors = []
    
    for prime in primes:
        prime_counter = 0
        add = False
        if prime < n_init//2 + 1:
            while n % prime == 0:
                add = True
                prime_counter += 1
                n = n//prime
            if add:
                factors.append(prime**prime_counter)
        else:
            break
    return factors

primes = prime_mod.list_primes(10**4)

def verify_factors(number, N):
    """
    n: integer
    N: succesive numbers, including n, to verify
    Returns Ture if ach n and its succesive numbers each have N different factors.
    """
    factors = []
    for n in range(number, number + N):
        new_factors = get_factors(n)
        if not len(new_factors) == N:
            return False
        else:
            factors.extend(new_factors)
    factors = set(factors)
    print(factors)
    if len(factors) == N*N:
        return True
    else:
        return False


N = 4
n = 2
primes = prime_mod.list_primes(1000)
while True:
    if verify_factors(n, N):
        print(n)
        break
    else:
        n += 1