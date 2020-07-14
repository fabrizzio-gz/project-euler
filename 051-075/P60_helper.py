import prime
import pickle

# Load previous files of 10**4 first primes and 10**4 maps
small, is_prime = pickle.load(open('save60.p', 'rb'))

# Get small list of 10'000 primes
N = 10**4
#minN = 10**4
small = prime.list_primes(N)
# Map of prime values up to N**2
is_prime = list(map(prime.is_prime, range(N**2)))

#small += small2
#is_prime += is_prime2
primes = [small, is_prime]
pickle.dump(primes, open( "save60.p", "wb" ))

