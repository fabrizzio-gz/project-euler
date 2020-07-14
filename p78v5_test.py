## 
# Problem 78
##
# Partition of coins in different piles.
from time import time
from math import ceil
from collections import deque

def p(past_sol, cumulative_results):
    """
    cumulative_results: results for the upper part, from 1 to n//2
    past_sol: list (deque) with cumulative solutions for less than n coins
    Returns a list of solutions: first_pile_coins : # solutions with as many as first_pile_coins.
    indexes are 0 for n = 1, 1 for n = 2 and n - 1 for n = n.
    Appends returned list to past solutions.
    """
    global n
    n += 1
    # Purge results from bottom half (erase detailed table for a single value)
    if n%2 == 0:
        # Get total piles from left end result
        cumulative_results.append((past_sol[0][n//2 - 1]) % 10**6)
        # Eliminate left item from past_sol
        past_sol.popleft()
    start = len(cumulative_results)
    n_sol = [1] # Initial solution for pile = 1
    # Bottom half
    half = ceil(n/2)
    for first_pile in range(2, half):
        rest_coins = n - first_pile 
        rest_coins_index_start = rest_coins - 1 - start
        first_pile_index = first_pile - 1
        # first_pile_index_start = first_pile_index - start 
        # Cumulate results
        n_sol.append((n_sol[first_pile_index - 1] + past_sol[rest_coins_index_start][first_pile_index]) % 10**6)
    
    # Upper part with purged results
    for first_pile in range(half, n):
        rest_coins = n - first_pile
        first_pile_index = first_pile - 1
        rest_coins_index = rest_coins - 1
        n_sol.append((n_sol[first_pile_index - 1] + cumulative_results[rest_coins_index]) % 10**6)
        #n_sol.append((n_sol[first_pile_index - 1] + past_sol[rest_coins_index][0]) % 10**6)
    # Last result. Only one possible pile for first_pile = n
    n_index = n - 1
    result = (n_sol[n_index - 1] + 1) % 10**6
    n_sol.append(result)
    past_sol.append(n_sol)
    return result

def print_special(piles, cumulative_results):
    global n
    s = sum(cumulative_results)
    print('{: >5} {: >10} {: >5} {: >5} {: >5}'.format(n, piles, s, piles - s, piles - s - 2))


past_sol = deque([])
# past_sol.append([1]) # partitions for 1 coin (not included for part of cumulative_results)
past_sol.append([1, 2]) # partitions for 2 coins
past_sol.append([1, 2, 3]) # partitions with 3 coins
cumulative_results = [1]
n = 3
start_time = time()
zero_time = time()
cond = True
print('{: >5} {: >10} {: >5} {: >5} {: >5}'.format('n', 'piles', 'sum', 'd1', 'd2'))
print('--------------------------------------')
while cond:
    for i in range(25):
        print_special(p(past_sol, cumulative_results), cumulative_results)
    break
    print('Current n = ', n)
    print('Elapsed time:', round(time() - start_time, 1))
    start_time = time()
    if n > 55000:
        for i in range(1000):
            if p(past_sol, cumulative_results) == 0:
                print('The answer is:', n)
                cond = False
#print('Total time: ', round(time() - zero_time, 1))
#print_special(past_sol)
#print(cumulative_results)