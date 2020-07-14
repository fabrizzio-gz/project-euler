from math import factorial

def next_chain(n):
    """
    Returns the sum of the factorials of n digits.
    """
    factorials = [factorial(int(digit)) for digit in str(n)]
    return sum(factorials)

def calculate_chain(n, chains_dict):
    if n in chains_dict:
        return chains_dict[n]
    if n == next_chain(n):
        chains_dict[n] = 1
        return 1
    val = 1 + calculate_chain(next_chain(n), chains_dict)
    chains_dict[n] = val
    return val

chains_dict = {0:2, 1:1, 2:1, 145:1,
               871:2, 45361:2,
               872:2, 45362:2,
               169:3, 363601:3, 1454:3}

count = 0
for n in range(1, 10**6):
    if calculate_chain(n, chains_dict) == 60:
        count += 1
print(count)



