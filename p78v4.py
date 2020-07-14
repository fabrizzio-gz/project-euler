## 
# Problem 78
##
# Partition of coins in different piles.
from time import time
from math import ceil

def p(past_sol):
    """
    n: total quantity of coins (n >= 3)
    past_sol: list with cumulative solutions for less than n coins
    Returns a list of solutions: first_pile_coins : # solutions with as many as first_pile_coins.
    indexes are 0 for n = 1, 1 for n = 2 and n - 1 for n = n.
    Appends returned list to past solutions.
    """
    global n
    n += 1
    n_sol = [1] # Initial solution for pile = 1
    # Bottom half
    half = ceil(n/2)
    for first_pile in range(2, half):
        rest_coins = n - first_pile 
        rest_coins_index = rest_coins - 1
        first_pile_index = first_pile - 1
        # Cumulate results
        n_sol.append((n_sol[first_pile_index - 1] + past_sol[rest_coins_index][first_pile_index]) % 10**6)
    # Purge results from bottom half (erase detailed table for a single value)
    if n%2 == 0:
        past_sol[n//2 - 1] = [(past_sol[n//2 - 1][n//2 - 1]) % 10**6]
    # Upper part with purged results
    for first_pile in range(half, n):
        rest_coins = n - first_pile
        first_pile_index = first_pile - 1
        rest_coins_index = rest_coins - 1
        n_sol.append((n_sol[first_pile_index - 1] + past_sol[rest_coins_index][0]) % 10**6)
    # Last result. Only one possible pile for first_pile = n
    n_index = n - 1
    result = (n_sol[n_index - 1] + 1) % 10**6
    n_sol.append(result)
    past_sol.append(n_sol)
    return result

def count_solutions(dict_):
    return sum(dict_.values())

past_sol = []
past_sol.append([1]) # partitions for 1 coin
past_sol.append([1, 2]) # partitions for 2 coins
past_sol.append([1, 2, 3]) # partitions with 3 coins
n = 3
start_time = time()
zero_time = time()
cond = True
while cond:
    for i in range(10):
        print(p(past_sol))
    print(past_sol)
    break
    print('Current n = ', n)
    print('Elapsed time:', round(time() - start_time, 1))
    start_time = time()
    if n > 55000:
        for i in range(1000):
            if p(past_sol) == 0:
                print('The answer is:', n)
                cond = False
print('Total time: ', round(time() - zero_time, 1))