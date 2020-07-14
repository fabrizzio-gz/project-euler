import pickle
from math import prod

from prime import is_prime

def is_permutation(num1, num2):
    """
    Check if num1 is a permutation of the digits of num2
    Rerturns True is yes. False if not.
    """
    num1_str = list(str(num1))
    num2_str = list(str(num2))
    if len(num1_str) != len(num2_str):
        return False
    if sorted(num1_str) == sorted(num2_str):
        return True
    return False

def calculate_phi_n(n, factors_dict):
    """
    Returns phi_n(n) using Euler's Product Formula.
    """
    global primes
    def get_factors(n):
        n_old = n
        if is_prime(n):
            factors_dict[n] = [n]
            return [n]
        factors = []
        for prime in primes:
            while n % prime == 0:
                factors.append(prime)
                n /= prime
                if n in factors_dict:
                    factors.extend(factors_dict[n])
                    n = 1
            if n == 1:
                break
        factors_dict[n_old] = list(set(factors))
        return list(set(factors))

    factors = get_factors(n)
    phi_n = n * prod([(1 - 1/p) for p in factors])
    return round(phi_n)

# numbers in the range 9 million - 10 million -> max n
primes = pickle.load(open('primes10million.p', "rb"))
min_phi = 10
phi_permutations = []
factors_dict = {}
for n in range(10, 10**7):
    phi_n = calculate_phi_n(n, factors_dict)
    if is_permutation(n, phi_n):
        if n/phi_n < min_phi:
            min_phi = n/phi_n
            print(f'Current minimun: {n/phi_n}, for n = {n}')
            phi_permutations.append((n, phi_n))
print(phi_permutations[-1])
            