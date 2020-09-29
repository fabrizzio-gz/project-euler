from math import factorial, prod
from itertools import combinations_with_replacement, combinations


def get_y(x, n):
    return x * n // (x - n)


def is_solution(x, y, n):
    return x * y // (x + y) == n


def count_solutions(n: int)-> int:
    # x = n + 1 and x = 2 * n always yield solutions
    solutions = 2 # x, y = 2n, 2n is a solution

    for x in range(n + 2, 2 * n):
        y = get_y(x, n)
        if is_solution(x, y, n):
            solutions += 1

    return solutions


def get_solution_from_factors(factors):
    """
    Factors must include 1.
    Get solutions by dividng n**2 into 2 different factors a, b.
    Count possible solutions as possible different a, b factors.
    Return possible solutions
    """
    # factors = get_factors(n)
    number_of_factors = len(factors)
    # Get all possible combinations with a <= b
    max_val = prod(factors)
    # n² formed by double factors of n
    factors = factors[:] + factors[:]
    
    # First solution with a = 1 b = n²
    solutions = 0
    solution_factors = []
    
    for factor_count in range(1, number_of_factors + 1):
        for factor_combination in combinations(factors, factor_count):
            factor_a = prod(factor_combination)
            if factor_a <= max_val and factor_a not in solution_factors:
                solutions += 1
                solution_factors.append(factor_a)

    return solutions


# Solution: Use count_solutions for numbers composed of largest number of factors. Trial and error from factors 1*2*3*5*7*11*13*17 and then reducing greatest factor: 13 by factor 2 and 17 by factor 3. (trial and error)
