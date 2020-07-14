"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated
 numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
 being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.
"""
import prime as prime_mod

# All valid only for numbers of 5 digits

def possible_nums(last_digit = '3'):
    """
    last_digit: an int, usually 3 or 7 to append to end of number
    Returns all possible combinations of numbers of the form **xx[last_digit] where * are 01-9 digits.
    x is a repeating digit.
    """
    digit_1iter = '123456789'
    digit_iter = '0123456789'
    number_list = []
    for digit1 in digit_1iter:
        for digit2 in digit_iter:
            for digitx in digit_iter:
                number = digit1 + digit2 + digitx*2 + last_digit
                number_list.append(int(number))
    return number_list

def possible_numsb(last_digit = '3'):
    """
    last_digit: an int, usually 3 or 7 to append to end of number
    Returns all possible combinations of numbers of the form *x*x[last_digit] where * are 01-9 digits.
    x is a repeating digit.
    """
    digit_1iter = '123456789'
    digit_iter = '0123456789'
    number_list = []
    for digit1 in digit_1iter:
        for digit2 in digit_iter:
            for digitx in digit_iter:
                number = digit1 + digitx + digit2 + last_digit
                number_list.append(int(number))
    return number_list

def possible_numsxxx(last_digit = '3'):
    """
    last_digit: an int, usually 3 or 7 to append to end of number
    Returns all possible combinations of numbers of the form x***[last_digit] where * are 01-9 digits.
    x is a repeating digit.
    """
    digit_1iter = '123456789'
    digit_iter = '0123456789'
    number_list = []
    for digit1 in digit_1iter:
        for digitx in digit_iter:
            number = digit1 + 3*digitx + last_digit
            number_list.append(int(number))
    return number_list

def get_reps(possible_primes, digits = [0, 1]):
    """
    possible_primes: list of int primes in the form **xx3 or **xx7
    digits: indexes to produce keys
    Returns, for each initial **, how many reps are present as a dictionary 2digits(key)-> #reps(value)
    """
    possible_primes_str = list(map(str, possible_primes))
    evals = {}
    index1 = digits[0]
    index2 = digits[1]
    for prime in possible_primes_str:
        key = prime[index1] + prime[index2]
        if not key in evals:
            evals[key] = len([prime for prime in possible_primes_str if prime[index1] + prime[index2] == key])
    return evals

def get_repsxxx(possible_primes):
    """
    possible_primes: list of int primes in the form *xxx[last_digit]
    Returns, for each initial *, how many reps are present as a dictionary 2digits(key)-> #reps(value)
    """
    possible_primes_str = list(map(str, possible_primes))
    evals = {}
    index1 = 0
    for prime in possible_primes_str:
        key = prime[index1]
        if not key in evals:
            evals[key] = len([prime for prime in possible_primes_str if prime[index1] == key])
    return evals


primes = prime_mod.list_primes(100000, 9999)
max_vals = 0
max_last_digit = '0'
for last_digit in '1379':
    possible_numbers = possible_numsxxx(last_digit)
    possible_primes = [prime for prime in primes if prime in possible_numbers]
    evals = get_repsxxx(possible_primes)
    max_vals = 0
    for key in evals:
        if evals[key] > max_vals:
            max_vals = evals[key]
            max_key = key
            max_last_digit = last_digit
    print('For last_digit', last_digit, 'got keys', evals)
print(max_key,'xxx', max_last_digit, ':', max_vals, )
