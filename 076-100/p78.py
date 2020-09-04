## 
# Problem 78
##
# Partition of coins in different piles.

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
    for first_pile in range(n - 2, 0, -1):
        solutions = 0
        rest_coins = n - first_pile
        next_piles_options = past_sol[rest_coins]
        if first_pile >= rest_coins:
            solutions +=  count_solutions(next_piles_options)
        else:
            for second_pile in range(1, first_pile + 1):
                solutions += next_piles_options[second_pile]
        n_sol[first_pile] = solutions
    past_sol[n] = n_sol
    return n_sol

def count_solutions(dict_):
    return sum(dict_.values())

past_sol = {}
past_sol[1] = {1:1}
past_sol[2] = {2:1, 1:1}
n_coins = 3
while True:
    solution_n = p(n_coins, past_sol)
    print(n_coins, count_solutions(solution_n))
    if count_solutions(solution_n) % 10**6 == 0:
        print(n_coins)
        break
    n_coins += 1


