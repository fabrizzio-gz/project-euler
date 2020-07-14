from math import gcd
from itertools import repeat
from prime import is_prime
from fractions import Fraction

def coprime(a, b):
    return gcd(a, b) == 1

def get_factors(x):
    """
    Returns a list of possible factors for x. Factors less than sqrt(x).
    For a factor n, the cofactor can be written as x//n.
    """
    global primes
    if primes[x]:
        return []
    factors = []
    for factor in range(2, int(x**.5)):
        if x%factor == 0:
            factors.append(factor)
    return factors

N = 100
max_ratio = 1
max_n = 0
primes = list(map(is_prime, range(0, N + 1)))
# List with phi_n values
list_phi_n = list(repeat(-1, N + 1))
list_ratio = list_phi_n[:]
# List of coprimity
list_coprimes = list(repeat(None, N + 1))
for index in range(len(list_coprimes)):
    # 0-> False. 1-> True
    list_coprimes[index] = [False, True]
print(list_coprimes)
for n in range(2, N + 1):
    # 1 is always coprime
    phi_n = 1
    # See if it's possible to express phi_n as phi(n.m) = phi(n).phi(m) [n, m coprimes]
    # for factor1 in get_factors(n):
    #     factor2 = n//factor1
    #     greater, lower = (factor1, factor2) if factor1 > factor2 else (factor2, factor1)
    #     # Check if factors are coprime
    #     if list_coprimes[greater][lower]: #coprime(factor1, factor2):
    #         list_phi_n[n] = list_phi_n[factor1]*list_phi_n[factor2]
    #         break
    # # Check if value isn't recorded. If not, calculate it.
    if list_phi_n[n] == -1:
        for test in range(2,n):
            if coprime(n, test):
                phi_n += 1
                list_coprimes[n].append(True)
            else:
                list_coprimes[n].append(False)
        else:
            list_phi_n[n] = phi_n
            list_ratio[n] = Fraction(n, phi_n)
            if n/phi_n > max_ratio:
                max_ratio = n/phi_n
                max_n = n
                print(n)
print(list_ratio)
print(max_ratio, max_n)
# for index, coprimes in enumerate(list_coprimes):
#     print(f'Coprime list for number {index}:\n {coprimes}')
    