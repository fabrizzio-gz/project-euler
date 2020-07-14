"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def sum_divisors(n):
    if n % 2 == 0:
        step = 1
    else:
        step = 2
    divisors = []
    if n == 4:
        return sum([1, 2])
    for div in range(1, int(n**.5) + 1, step):
        if n % div == 0:
            div2 = n//div
            divisors.append(div)
            if div2 != div and div2 != n:
                divisors.append(div2)
    #print('The divisors of', n,'are', divisors)
    return sum(divisors)

amicable = []
for n1 in range(2, 10000):
    if n1 not in amicable:
        n2 = sum_divisors(n1)
        if sum_divisors(n2) == n1 and n2 != n1:
            amicable.append(n1)
            amicable.append(n2)
print(amicable)
print(sum(amicable))
