##
# Problem 92
##
# Calculating chain numbers below 10mill that
# end with 89.

# Idea: get chains with memoization.
from time import time()

def next_chain(n, previous_chains):
    """
    n: an integer
    previous_chains: a list of integers.
    Calculates next chain adding the square of the digits of n.
    Returns either 1 or 89.
    """
    previous_chains.append(n)
    global chains
    number_chain = sum([int(digit)**2 for digit in str(n)])
    if chains[number_chain] != 0:
        return chains[number_chain], previous_chains
    else:
        return next_chain(number_chain, previous_chains)

        
def add_chains(previous_chains, chain_end, chains):
    """
    previous_chains: A list of integers.
    chain_end: An integer.
    chains: A list of integers.
    Updates the values chains[previous_chains[i]] = chain_end
    """
    for chain in previous_chains:
        chains[chain] = chain_end
    return None


max_val = 10**7
# List to memoize chains
chains = [0] * (max_val + 1)
chains[1] = 1
chains[89] = 89
count = 0
for i in range(1, max_val + 1):
    previous_chains = []
    chain_end, previous_chains = next_chain(i, previous_chains)
    if chain_end == 89:
        count += 1
    add_chains(previous_chains, chain_end, chains)
print(count)
