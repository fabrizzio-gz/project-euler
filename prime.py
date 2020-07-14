def is_prime(n):
    """
    n is an integer number 
    returns True if n is prime, False otherwise
    """
    assert type(n) == int, 'Not a valid input (int)'
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check only odd divisors
    for divisor in range(3,int(n**.5)+1,2):
        if n % divisor == 0:
            return False
    return True

def list_primes(n, min_n = 1):
    """
    n is an integer > 0
    min_n: lower limit
    Returns a list of all the primes <= n
    """
    #map_primes = list(map(is_prime, range(1, n + 1)))
    #prime_vals = [index + 1 for index in range(len(map_primes)) if map_primes[index]]
    map_primes = list(map(is_prime, range(min_n, n + 1)))
    prime_vals = [index + min_n for index in range(len(map_primes)) if map_primes[index]]
    return prime_vals

def prime_gen(start = 3):
    """
    Generator. Produces succesive prime numbers starting from 3
    """
    prime = start
    while True:
        is_prime = True
        for divisor in range(3,int(prime**.5)+1,2):
            if prime % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 2

def main():
    a = prime_gen()
    counter = 0
    for i in a:
        counter += 1
        print(i)
        if counter > 100:
            break
    

if __name__ == "__main__":
    main()
