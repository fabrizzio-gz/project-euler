"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating 
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four 
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce 
another prime.
"""
import prime as prime_mod
import pickle

def concatenates_prime(list_primes, primex):
    """
    list_prime: a list of primes to compare
    prime: a prime (int) to concatenate with all primes in list and see if it produces primes
    Returns True if prime concatenates with all primes in list_primes, False if not
    """
    # List of primes
    global small
    global is_prime
    for prime in list_primes:
        # Concatenate front prime + primex
        order = len(str(primex))
        prime0 = prime * 10**order
        primef = prime0 + primex
        if primef < len(is_prime):
            if not is_prime[primef]:
                break
        elif not prime_mod.is_prime(primef):
            break
        # Concatenate back primex + prime
        order = len(str(prime))
        primex0 = primex * 10**order
        primeb = primex0 + prime
        if primeb < len(is_prime):
            if not is_prime[primeb]:
                break
        elif not prime_mod.is_prime(primeb):
            break
    else:
        # Once all values have been verified and no break
        return True
    # When 'break'
    return False

def get_primes(n):
    """
    n: an integer
    Returns a list of 'n' primes that concatenate to primes
    """
    # List of primes
    global small
    global is_prime
    primes = []
    for i in range(len(small)):
        # The lists starts with primei to concatenate with all possible primes
        primes = [small[i]]
        for j in range(len(small)):
            primej = small[j]
            if concatenates_prime(primes, primej):
                primes.append(primej)
                # Check value is achieved
                if len(primes) >= 4:
                    print('A list of len', str(len(primes)),':', primes)
    else:
        # Ran through all  possible values with no luck
        return []
            
def get_prime(list_primes):
    """
    list_primes: a list of numbers
    Mutates list_primes and concatenates the next prime that concatenates with all values
    """
    start = list_primes[-1]
    #start = 10**4 - 1
    prime_gen = prime_mod.prime_gen(start + 2)
    while True:
        prime = next(prime_gen)
        if concatenates_prime(list_primes, prime):
            list_primes.append(prime)
            print(prime)
            break

# small: list of primes < 10K and is_prime is an index of primes up to 10**8 (N**2)
small, is_prime = pickle.load(open('save60.p', 'rb'))

# List of primes that concatenate already:
#list_primes = [3, 7] #, 109, 673]
#get_prime(list_primes)
#print(list_primes)
get_primes(5)


emp_2
emp_2
emp_2


