from math import gcd

def coprime(a, b):
    return gcd(a, b) == 1

low_b = 1/3
up_b = 1/2
N = 12000
count = 0
for denom in range(2, N + 1):
    for num in range(int(.3 * denom), denom):
        if coprime(num, denom):
            f = num/denom
            if f > low_b:
                if f >= up_b:
                    break
                else:
                    count +=1
print(count)