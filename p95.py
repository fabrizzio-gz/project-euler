##
# Problem 95
##

# Finding smallest number of longest chain with numbers less than 1 million

# Idea: iterate chains and memoization
import sys
from time import time

def get_factors(n):
    factors = []
    global primes
    for prime in primes:
        if n != 1:
            while n % prime == 0:
                n /= prime
                factors.append(prime)
        else:
            break
    return factors

def get_divisors(n):
    divisors = [1]
    for divisor in range(2, int(n**.5)):
        if n % divisor == 0:
            divisors.append(divisor)
            divisors.append(n//divisor)
    sqrt = int(n**.5)
    if sqrt**2 == n:
        divisors.append(sqrt)
    return divisors


def next_chain(n):
    return sum(get_divisors(n))


def calculate_chain(n, past_chains, limit):
    next_ = next_chain(n)
    if next_ == 1 or next_ > limit:
        return 0, past_chains
    if next_ in past_chains:
        if next_ == past_chains[0]:
            return len(past_chains), past_chains
        else:
            return 0, past_chains
    else:
        past_chains.append(n)
        return calculate_chain(next_, past_chains, limit)


def update_chain(new_chain, numbers_in_chains):
    for chain in new_chain:
        numbers_in_chains[chain] = True

def main(limit):
    start = time()
    numbers_in_chains = [False] * (limit + 1)
    max_chain = 0
    smallest = 0
    for n in range(2, limit + 1):
        if not numbers_in_chains[n]:
            chain, new_chain = calculate_chain(n, [n], limit)
            update_chain(new_chain, numbers_in_chains)
            if chain > max_chain:
                max_chain = chain
                smallest = n
    print("The largest chain was {}. With smallest number: {}".format(max_chain, smallest))
    print("Elapsed: {} s".format(round(time() - start, 2)))

main(int(sys.argv[1]))

# Example usage:
# $ python3 p95.py <limit>
