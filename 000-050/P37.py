import prime as prime_mod

def prime_gen():
    """
    Generator. Produces succesive prime numbers starting from 3
    """
    prime = 3
    while True:
        is_prime = True
        for divisor in range(3,int(prime**.5)+1,2):
            if prime % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 2

def trunc_prime(prime, primes):
    """
    prime: is any prime number
    primes: list of all primes up to prime.
    Returns True if truncated numbers from right and left are all primes as well.
    """
    prime_str = str(prime)
    for index in range(1,len(prime_str)):
        primeL = int(prime_str[:-index])
        if primeL not in primes:
            return False
        primeR = int(prime_str[index:])
        if primeR not in primes:
            return False
    return True


truncated_primes = []
primes = [2]
prime_values = prime_mod.prime_gen()
while len(truncated_primes) < 11:
    prime = next(prime_values)
    primes.append(prime)
    if trunc_prime(prime, primes):
        if prime > 10:
            print(prime)
            truncated_primes.append(prime)
print(truncated_primes)
print(sum(truncated_primes))

    


