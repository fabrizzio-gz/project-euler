"""
Euler discovered the remarkable quadratic formula: n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive 
values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n2+an+b

, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces the 
maximum number of primes for consecutive values of n, starting with n=0.
"""
import prime

def evaluate_quad(a,b,n):
    """
    a integer between (-1000 , 1000)
    b integer between [-1000, 1000]
    n integer > 0
    Returns True if n^2 + a*n + b is prime. False if not.
    """
    assert all([type(x) == int for x in (a, b, n)]), "Invalid input (int)"
    quad = n**2 + a*n + b
    return is_prime(quad)

def quad_function(a,b):
    """
    a integer between (-1000 , 1000)
    b integer between [-1000, 1000]
    Returns function handle f(n) = n^2 + a*n + b
    """
    return lambda n: n**2 + a*n + b

def max_consecutive_n(quad):
    """
    quad is a function handle of the form f(n) = n^2 + a*n + b
    returns maximum consecutive integer such that f(n) is integer
    """
    n = 0
    while prime.is_prime(quad(n)):
        n += 1
        if quad(n) <= 0:
            # Not possible
            return 0
    return n - 1

# Quad conditions: b -> prime, b >0 b <=1000
# a > -b (odd)  a: [-b , 1000)
max_n, max_b, max_a = 0, 0, 0
# list_primes produces a list of primes < 1000
b = prime.list_primes(1000)
for b_param in b:
    for a in range(-b_param,1000,2):
        # quad is a function handle for f(n) = n^2 + a*n + b
        quad = quad_function(a,b_param)
        # max_consecutive_n returns the greatest consecutive number giving a prime
        n = max_consecutive_n(quad)
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b_param
print(max_n, max_a, max_b)
