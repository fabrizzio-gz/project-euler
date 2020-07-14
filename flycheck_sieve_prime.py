sieve = [True] * 101
limit = 100
primes = []
for n in range(2, limit + 1):
    if sieve[n]:
        primes.append(n)
        multiple = 2*n
        while multiple <= limit:
            sieve[multiple] = False
            multiple += n
print(primes)
