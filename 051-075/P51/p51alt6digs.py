import re
import itertools
import prime

### It works with 6 digits: 1xxxx[ld]
### TO RUN
print('Alt: 6 digits 1xxxx[ld]')
# Creating possible permutations
tuples = list(itertools.permutations('1xxxx', 5))
permutations = list(map(str.join, ['']*len(tuples),tuples ))

# Creating list of primes
primes = prime.list_primes(1000000, 99999)
primes = list(map(str, primes))

digits = '0123456789'
lastdigits = '1379'

max_count = 0
max_key = 'x'
key_list = []
for permutation in permutations:
    for digit1 in digits:
        for digitx in digits:
            for lastdigit in lastdigits:
                key = permutation.replace('1', digit1)
                key += lastdigit
                #print(key)
                if not key[0] == '0':
                    if not key in key_list:
                        key_list.append(key)
                        # Creating expression
                        expression = key.replace('x','(.)',1).replace('x','\\1{1}')
                        r = re.compile(expression)
                        count = len(list(filter(r.match, primes)))
                        print(expression, count) 
                        if count > max_count:
                            print(key, ':', count)
                            max_count = count
                            max_key = key
print(max_key, ':', max_count)