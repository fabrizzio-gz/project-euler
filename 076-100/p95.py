##
# Problem 95
##

# Finding smallest number of longest chain with numbers less than 1 million

# Idea: iterate chains and memoization
import sys
from time import time

def proper_divisors(n):
    """
    n: an integer > 1
    Returns a list with the proper divisors of n.
    Returns an empty list if n = 1
    """
    if n == 1:
        return []
    divisors = [1]
    # Check if n is a perfect square
    # Modify upper limit of divisors accordingly
    sqrt_n = int(n**.5)
    if n**.5 == sqrt_n:
        divisors.append(sqrt_n)
        upper_limit = sqrt_n
    else:
        upper_limit = sqrt_n + 1
        
    for divisor in range(2, upper_limit):
        if n % divisor == 0:
            divisors.append(divisor)
            divisors.append(n // divisor)
    return divisors


def is_amicable_chain(n):
    """
    n: an integer > 1
    Returns True if n is part of an amicable chain.
    Returns False if not.
    """
    pass


def get_chain(n, chain = None, start = None):
    """
    n: An integer > 1
    chain: A list of numbers that come before n in a proper divisor chain.
    start: First value of the chain.
    Returs a tuple with a listof the chain of proper divisors and the value that comes
    next in the chain.
    Conditions to stop producing the chain:
    - chain reaches 1.
    - chain returns to its first value.
    - chain enters an inner loop.
    - Next value in chain is larger than allowed limit.
      Return chain and limit value instead of next_chain in that case.
    """
    # Maximum value that must not be surpassed.
    global LIMIT

    # Append n as starting value.
    if not chain:
        chain = [n]

    # Create starting point for the chain
    if not start:
        start = n
        
    if n == 1:
        return chain, None
    
    next_chain = sum(proper_divisors(n))
    
    if next_chain > LIMIT:
        return chain, 0
    elif next_chain in chain:
        return chain, next_chain
    else:
        chain.append(next_chain)
        return get_chain(next_chain, chain, start)

    
def update_chains(calculated_chains, chain):
    """
    calculated_chains: A list of True/False.
    chain a list of integers belonging to an amicable chain.
    Updates all indexes from chains to 'True' on calculated_chains.
    """
    for n in chain:
        calculated_chains[n] = True


def main():
    global LIMIT
    start = time()
    amicable_chains = []
    for n in range(2, LIMIT + 1):
        if not calculated_chains[n]:
            chain, last_value = get_chain(n)
            #update_chains(calculated_chains, chain)
            if last_value == n:
                print('Amicable chain at {}!'.format(n))
                update_chains(calculated_chains, chain)
                amicable_chains.append(chain)

    longest_chain = sorted(amicable_chains, key=len, reverse=True)[0]
    print('The smallest value of the longest chain is {}'.format(min(longest_chain)))
    print('Elapsed time: {}'.format(round(time() - start, 2)))

    
LIMIT = int(sys.argv[1])
calculated_chains = [False] * (LIMIT + 1)
main()
# Usage:
# $ python3 p95.py <limit>
