import re
import itertools
import prime

# Creating possible permutations
tuples = list(itertools.permutations('123xx', 5))
permutations = list(map(str.join, ['']*len(tuples),tuples ))

# Creating list of primes
primes = prime.list_primes(100000, 9999)
primes = list(map(str, primes))

digits = '0123456789'
lastdigits = '1379'

max_count = 0
max_key = 'x'
for permutation in permutations:
    for digit1 in digits:
        for digit2 in digits:
            for digitx in digits:
                for digit3 in digits:
                    key = permutation.replace('1', digit1).replace('2', digit2).replace('3', digit3)
                    # Creating expression
                    expression = key.replace('x','(.)',1).replace('x','\\1{1}')
                    r = re.compile(expression)
                    count = len(list(filter(r.match, primes))) 
                    if count > max_count:
                        print(key, ':', count)
                        max_count = count
                        max_key = key
print(max_key, ':', max_count)