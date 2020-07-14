from time import time

def pentagonal_n(start = False):
    """
    Yields the next pentagon number using Pk = k(3k - 1)/2
    with k = 1, -1, 2, -2
    """
    def P(k):
        return k*(3*k -1)//2
    k = 1
    while True:
        yield P(k)
        yield P(-k)
        k += 1

def p(partitions):
    """
    Recursively calculates p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + ...
    """
    global n
    n += 1
    p = 0 # partitions
    k1, k2 = 0, 0 # indices
    summator = 1 # To alternate signs
    ki = pentagonal_n()
    while True:
        index1 = n - next(ki)
        if index1 >= 0:
            p += summator*partitions[index1]
        else:
            break
        index2 = n - next(ki)
        if index2 >= 0:
            p += summator*partitions[index2]
        else:
            break
        summator *= -1
    p %= 10**6
    partitions.append(p)
    return p


partitions = []
partitions.append(1) # p(0) = 1
n = 0 # First number
start = time()
while True:
    if p(partitions) == 0:
        print('Elapsed time:', round(time() - start, 1), 'n =', n)
        break
    

