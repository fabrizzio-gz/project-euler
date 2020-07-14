##
# Problem 77
##

# Find the possible ways to write a number as a sum of primes

from prime import is_prime

def solve(n, solutions):
    """
    Calculates the possible ways to write n as a prime or
    as a sum of primes.
    solutions: A dictionary with prior solutions for numbers < n.
    Returns a list with the first addend of all solutions.
    """
    solutions_n = []
    if is_prime(n):
        solutions_n.append(n)
    # Next solutions in the form: first_addend + rest
    for rest in range(1, n - 1):
        first_addend = n - rest
        if is_prime(first_addend):
            # Get possible solutions, None if empty
            possible_addends = solutions.get(rest)
            if possible_addends:
                # Counter of addends greater than n
                for second_addend in possible_addends:
                    if second_addend <= first_addend:
                        solutions_n.append(first_addend)
    solutions[n] = solutions_n
    return solutions_n

solutions = {}
solutions[1] = []
answer = 0
for n in range(2, 100):
    if is_prime(n):
        prime_addend = 1
    else:
        prime_addend = 0
    possible_sums = len(solve(n, solutions)) - prime_addend
    if possible_sums > 5000:
        answer = n
        break
print(answer)
