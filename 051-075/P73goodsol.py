
from functools import lru_cache
from math import gcd, floor, ceil
from time import time

MAX_D = 12_000
LOWER = 1 / 3
UPPER = 1 / 2

@lru_cache(maxsize=None)
def n_fractions(d):
	if d < 4: return 0
	out = 0
	for n in range(int(LOWER * d) + 1, int(UPPER * d) + 1):
		if gcd(n, d) == 1: out += 1
	return out + n_fractions(d - 1)

start = time()
# caching to avoid stack overflow
for i in range(MAX_D):
	n_fractions(i)

ans = n_fractions(MAX_D)
stop = time()

print(f'Result: {ans}')
print(f'Time: {stop - start:4e}s')