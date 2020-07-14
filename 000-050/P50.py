"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import prime as prime_mod

def most_consecutive(primes, limit):
    """
    primes: a list of integers
    limit: maximum possible value of sum
    Returns the integer in primes that is the sum of the most succesive values in primes
    """
    max_consecutive = 0
    best = 0
    for i in range(len(primes)-1):
        for j in range(i + 1 + max_consecutive, len(primes)):
            consecutive_sum = sum(primes[i: j + 1])
            if consecutive_sum > limit:
                break
            if consecutive_sum in primes:
                index_diff = j - i
                if index_diff > max_consecutive:
                    best = consecutive_sum
                    max_consecutive = index_diff
    return best
    
limit = 10**6
primes = prime_mod.list_primes(limit)
print(most_consecutive(primes, limit))