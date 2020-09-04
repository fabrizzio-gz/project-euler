## 
# Problem 78
##
# Partition of coins in different piles.
from time import time

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
    n_sol = [1]
    for first_pile in range(2, n):
        rest_coins = n - first_pile 
        max_size = min(first_pile, rest_coins) 
        rest_coins_index = rest_coins - 1
        first_pile_index = first_pile - 1
        max_size_index = max_size - 1
        # Cumulate results
        n_sol.append(n_sol[first_pile_index - 1] + past_sol[rest_coins_index][max_size_index])
    # Only one possible pile for first_pile = n
    n_index = n - 1
    result = n_sol[n_index - 1] + 1
    n_sol.append(result)
    past_sol.append(n_sol)
    return result

def count_solutions(dict_):
    return sum(dict_.values())

past_sol = []
past_sol.append([1]) # partitions for 1 coin
past_sol.append([1, 2]) # partitions for 2 coins
n = 2
start_time = time()
while True:
    for i in range(1000):
        p(past_sol)
    print('Current n = ', n)
    print('Elapsed time:', round(time() - start_time, 1))
    start_time = time()
    if n > 55000:
        for i in range(1000):
            if p(past_sol) % 10**6 == 0:
                print(n)
    
# n_coins = 3
# while True:
#     solution_n = p(n_coins, past_sol)
#     print(n_coins, count_solutions(solution_n))
#     if count_solutions(solution_n) % 10**6 == 0:
#         print(n_coins)
#         break
#     n_coins += 1


