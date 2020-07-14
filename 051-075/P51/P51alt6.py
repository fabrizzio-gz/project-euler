import re
import itertools
import prime

# Same as alt5 but works with 1 x and 4 vars: 123x[ld]

# Creating possible permutations
tuples = list(itertools.permutations('123x', 4))
permutations = list(map(str.join, ['']*len(tuples),tuples ))

# Creating list of primes
primes = prime.list_primes(100000, 9999)
primes = list(map(str, primes))

digits = '0123456789'
lastdigits = '1379'

max_count = 0
max_key = 'x'
key_list = []
for permutation in permutations:
    for digit1 in digits:
        for digit2 in digits:
            for digit3 in digits:
                for digitx in digits:
                    for lastdigit in lastdigits:
                        key = permutation.replace('1', digit1).replace('2', digit2).replace('3', digit3)
                        key += lastdigit
                        #print(key)
                        if key[0] != '0':
                            if key not in key_list:
                                print(key)
                                key_list.append(key)
                                # Creating expression
                                expression = key.replace('x','(.)',1)
                                r = re.compile(expression)
                                count = len(list(filter(r.match, primes))) 
                                if count > max_count:
                                    print(key, ':', count)
                                    max_count = count
                                    max_key = key
print(max_key, ':', max_count)