"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 
to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import prime as prime_mod
import itertools

digits = '123456789'
max_prime = 0
for index_slice in range(9,2,-1):
    digits_slice=digits[:index_slice]
    numbers = list(itertools.permutations(digits_slice, len(digits_slice)))
    numbers = list(map(int, (map(str.join, ['']*len(numbers), numbers))))
    for number in numbers:
        if prime_mod.is_prime(number):
            if number > max_prime:
                max_prime = number
print(max_prime)