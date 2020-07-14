import pickle
from math import prod

from prime import is_prime

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

primes = pickle.load(open('primes1million.p', "rb"))
factors_dict = {}
N = 10**6
# The number of possible reduced fractions for each denominator equals phi(denominator)
count = 0
for denom in range(2, N + 1):
    count += calculate_phi_n(denom, factors_dict)
print(count)
