import prime as prime_mod
import pickle

def concatenates_prime(list_primes, primex):
    """
    list_prime: a list of primes to compare
    prime: a prime (int) to concatenate with all primes in list and see if it produces primes
    Returns True if prime concatenates with all primes in list_primes, False if not
    """
    # List of True/False indexes for primes below 10**8
    global is_prime
    for prime in list_primes:
        # Concatenate front prime + primex
        order = len(str(primex))
        prime0 = prime * 10**order
        primef = prime0 + primex
        if not prime_mod.is_prime(primef):
            break
        # Concatenate back primex + prime
        order = len(str(prime))
        primex0 = primex * 10**order
        primeb = primex0 + prime
        if not prime_mod.is_prime(primeb):
            break
    else:
        # Once all values have been verified and no break
        return True
    # When 'break'
    return False

# small: list of primes < 10K and is_prime is an index of primes up to 10**8 (N**2)
#small, is_prime = pickle.load(open('save60.p', 'rb'))

# Primes of 7-5 digits, mo
primes5 = prime_mod.list_primes(10**7, 10**5)

# list_primes =[3, 7, 109, 673]
# List of list of 4 primes that concatenate
list_list_primes = [[7, 19, 97, 3727], [11, 23, 743, 1871], [19, 31, 181, 9679], [23, 47, 1481, 4211], [43, 97, 1381, 8521], \
     [89, 107, 1061, 4973], [467, 587, 617, 6323], [1283, 1619, 4127, 7949], \
         [3391, 3433, 3643, 6607], [3547, 3643, 5449, 9817], [5023, 5443, 6841, 7039],\
             [5197, 5701, 6733, 8389], [6569, 6689, 6779, 8537]] 
for list_primes in list_list_primes:
    for primex in primes5:
        if concatenates_prime(list_primes, primex):
            print('At last!')
            print('List:', list_primes)
            print('Value:', primex)
            print('----')
            break
