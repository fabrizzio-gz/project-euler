from prime import is_prime
#from utility import factor


nums = []
for n in range(2, 1000001):
    if is_prime(n): continue
    nums.append(n)

def phi(n):
    res = n
    Nfac = factor(n)
    for f in Nfac:
        res = res*(1 - 1/f)
    return res

prior = 0
for item in nums:
    ph = phi(item)
    val = item/ph
    if val > prior:
        prior = val
        print(item, ph, val)