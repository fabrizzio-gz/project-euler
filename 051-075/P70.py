from math import gcd

def coprime(a, b):
    return gcd(a, b) == 1

def is_permutation(num1, num2):
    """
    Check if num1 is a permutation of the digits of num2
    Rerturns True is yes. False if not.
    """
    num1_str = list(str(num1))
    num2_str = list(str(num2))
    if len(num1_str) != len(num2_str):
        return False
    if num1_str.sort() == num2_str.sort():
        return True
    return False


# numbers in the range 9 million - 10 million -> max n
phi_permutations = []

for n in range(9*10**6, 10**7):
    phi_n = 0
    not_coprime = 0
    # Condition for phi_n > 10**6
    possible_fails = n - 10**6
    # phi_n between 1 million - 2 million -> min n
    for test in range(1, n):
        if coprime(test, n):
            phi_n += 1
        else:
            not_coprime += 1
        if not_coprime > possible_fails:
            break
        if phi_n > 2*10**6:
            break
    else:
        if is_permutation(n, phi_n):
            print(n, phi_n)
            phi_permutations.append(n/phi_n)
print(min(phi_permutations))
            