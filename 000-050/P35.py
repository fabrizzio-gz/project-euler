"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import prime as prime_mod

def produce_iterations(digits):
    """
    digits is a string of digits (0-9)
    Returns a list of all integers (as strings) that can be produced with list digits' digits.
    """
    digit_iterations = []
    if len(digits) == 1:
        return list(digits[0])
    else:
        for index in range(len(digits)):
            new_digits = digits[:index] + digits[index+1:]
            new_iterations = produce_iterations(new_digits)
            for iteration in new_iterations:
                digit_iterations.append(digits[index] + iteration)
        return set(digit_iterations)

def is_circular(prime):
    """
    prime_num is a prime number.
    Returns true if prime is a circular prime. False Otherwise
    """
    digits = str(prime)
    rotations = produce_rotations(digits)
    for num in rotations:
        if not prime_mod.is_prime(num):
            return False
    return True

def produce_rotations(digits):
    """
    digits is a string of digits (0-9)
    returns a list of ints of all rotation of digts. Ex: '21' returns 21 and 12
    """
    rotations = []
    for index in range(len(digits)):
        rotation = digits[index:] + digits[:index]
        if rotation not in rotations:
            rotations.append(rotation) 
    rotations = list(map(int, rotations))
    return rotations

def main():
    primes = set(prime_mod.list_primes(10**6))
    circular_primes = []

    for prime in primes:
        if prime not in circular_primes:
            rotation_primes = produce_rotations(str(prime))
            if set(rotation_primes).issubset(primes):
                circular_primes.extend(rotation_primes)

    print(circular_primes)
    print(len(circular_primes))

if __name__ == "__main__":
    main()