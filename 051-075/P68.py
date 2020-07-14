from itertools import permutations

# Digit 10 will be at one corner. Permutate over all
# the other combinations of the other 9 digits.
# Variables A-E: interior nodes of the pentagon.
# Variables a-e: each one of the "external nodes" 
# of the magic-pentagon.
# To each digit, asign one variable A-E b-e

# Possible values
digits = '123456789'
# Value fixed
a = 10
for permutation in permutations(digits):
    A, B, C, D, E, b, c, d, e = map(int, permutation)
    # Verify permutation is valid:
    if a + A + B == b + B + C == c + C + D == d + D + E == e + E + A:
        print('Permutation valid! Sum:', a + A + B)
        print(A, B, C, D, E, a, b, c, d, e)
        print('-----')

