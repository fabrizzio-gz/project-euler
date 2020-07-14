from math import gcd

# Using pythagorean triple approach:
# a = m.n
# b = 1/2(m^2 - n^2)
# c = 1/2(m^2 + n^2)
# n < m, odd

m = 3
L = 0
# List of possible sum(a + b + c)
LIMIT = 1.5*10**6 #1.5 * 10**6
list_L = []
# Calculating primitives
while L <= LIMIT:
    # To check if values reached limit: L > 1.5 million 
    first = True
    for n in range(1, m, 2):
        if gcd(m, n) == 1:
            a = m*n
            b = int((m**2 - n**2)/2)
            c = int ((m**2 + n**2) / 2)
            total = a + b + c
            if first:
                first = False
                L = total
            if total > LIMIT:
                break
            list_L.append(total)
    # m is odd
    m += 2

# Generating multiples of primitivessolutions 
solutions = {}
for L in list_L:
    mult = 1
    while L*mult <= LIMIT:
        solutions[L*mult] = solutions.get(L*mult, 0) + 1
        mult += 1

count = 0
for key in solutions:
    if solutions[key] == 1:
        count += 1 
print(count)