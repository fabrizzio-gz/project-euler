## 
# Problem 78
##
# Partition of coins in different piles.
import pickle

def p(n, past_sol):
    """
    n: total quantity of coins (n >= 3)
    past_sol: dictionary with solutions for less than n coins
    Returns a dictionary with: first_pile_coins : # solutions.
    Appends returned dictionary to past solutions.
    """
    n_sol = {}
    # A first unique pile of n coins
    n_sol[n] = 1
    # Second pile of n-1 coins and 1 coin
    n_sol[n-1] = 1
    # Analyze first_pile > second_pile first
    for first_pile in range(n - 2, n//2, -1):
        rest_coins = n - first_pile
        next_piles_options = past_sol[rest_coins]
        n_sol[first_pile] = count_solutions(next_piles_options)
    # Analyze second_pile > first_pile
    for first_pile in range(n//2, 0, -1):
        solutions = 0
        rest_coins = n - first_pile
        next_piles_options = past_sol[rest_coins]
        # Get all second_piles such that second_pile <= first_pile
        for second_pile in range(1, first_pile + 1):
            solutions += next_piles_options[second_pile]
        n_sol[first_pile] = solutions
    past_sol[n] = n_sol
    return n_sol

def count_solutions(dict_):
    return sum(dict_.values())

## To start from 0:
# past_sol = {}
# past_sol[1] = {1:1}
# past_sol[2] = {2:1, 1:1}
## To load:
f = open('p78_results.pkl', 'rb')
past_sol = pickle.load(f)
step = 1000
for _ in range(10):
    n_coins = max(past_sol.keys()) + 1
    for i in range(step):
        solution_n = p(n_coins, past_sol)
        if count_solutions(solution_n) % 10**6 == 0:
            print(n_coins)
            break
        n_coins += 1
    # Save past results
    with open('p78_results.pkl', 'wb') as f:
        pickle.dump(past_sol, f)
    n_coins -= 1
    print(n_coins, count_solutions(solution_n))
print('Done')

# To load:
# f = open('p78_results.pkl', 'rb')
# past_sol = pickle.load(f)