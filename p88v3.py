##
# Problem 88
##
# Finding the sum of minimum prodcut-sum for sets of numbers.

# Idea: test numbers increasingly using prime decomposition.
import prime as prime_mod
from math import prod
from time import time

def get_partitions(collection):
    # From: https://stackoverflow.com/questions/19368375/set-partitions-in-python
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in get_partitions(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def factor_decomposition(n):
    """
    n: an integer
    primes: list of prime factors
    Returns a list of n prime factors.
    """
    global primes
    global factor_list
    max_n = len(factor_list) - 1 # Value with largest n memoized
    if n <= max_n:
        return factor_list[n]
    factors = []
    for prime in primes:
        while n % prime == 0:
            n = n//prime
            factors.append(prime)
        if n == 1:
            break
    factor_list.append(factors)
    return factors

def get_product_combination(n):
    """
    n: an integer
    Returns all possible product combinations of those factors.
    """
    def clean(products):
        """
        products: a list of list of products
        Returns the same list without repeated elements.
        """
        new_products = []
        for product in products:
            if product not in new_products:
                new_products.append(product)
        return new_products
    
    global product_list
    n_max = len(product_list) - 1
    if n <= n_max:
        return product_list[n]
    
    factors = factor_decomposition(n)
    products = []
    for partition in get_partitions(factors):
        products.append(sorted(list(map(prod, partition))))
    products = clean(products)
    product_list.append(products)
    return products

def calculate_min_prod(k, start):
    """
    k: length of set of factors, addends.
    val: integer to start test with
    Returns minimum possible product-sum starting from 'val'
    """
    while True:
        for combination in get_product_combination(start):
            ones = k - len(combination)
            if prod(combination) == sum(combination) + ones:
                #print(combination)
                return start
        start += 1
factor_list = [[], [], [], []] # adding dummy values for n = 0 - 3
product_list = [[], [], [], []] # dummy values for n = [0 - 3]
start_time = time()
primes = prime_mod.list_primes(10**5)
end = 12000
sum_ = []
start = 4 # first factor to test
for k in range(2, end + 1):
    val = calculate_min_prod(k, start)
#    print(k, val)
    sum_.append(val)
    # if next_ != start:
    #     sum_ += next_
    #     start = 4 # next_
sum_ = set(sum_)
print(sum(sum_), round(time() - start_time, 2))
#print(sum_, round(time() - start_time, 2))
