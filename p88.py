##
# Problem 88
##
# Sets of minimal product-sum numbers for 2<=k<=12000
from itertools import combinations_with_replacement
from math import prod
from time import time

def get_sp(k):
    """
    k: number of addends/factors (k >= 2).
    Returns the minimum sum-product number for sets of size k.
    """
#    breakpoint()
    max_factor = 2
    while True:
        #print(max_factor)
        factors = range(1, max_factor + 1)
        factor_combinations = combinations_with_replacement(factors, k)
        for combination in factor_combinations:
            sum_comb = sum(combination)
            prod_comb = prod(combination)
            #print(combination)
            #print('Sum: {} Product: {}'.format(sum_comb, prod_comb))
            if prod_comb == sum_comb:
                return sum_comb
            elif prod_comb > sum_comb:
                # Product will only grow larger from this point
                break
        max_factor += 1

start = time()
end = 100
min_p_sums = set()
for k in range(2, end + 1):
    val = get_sp(k)
    print(k, val)
    min_p_sums.add(val)
end = time()
print(sum(min_p_sums), round(end - start, 2))
