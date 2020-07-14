"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
def is_prime(number):
    condition = True
    for i in range(2,number):
        if number % i == 0:
            condition = False
    return condition


n = 600851475143
maxi = 0
condition = True

div = 2

while condition:
    if is_prime(div) and n % div == 0:
        power = True
        while power:
            if n % div == 0:
                n = n // div
            else:
                power = False
        if div > maxi:
            maxi = div
    if n == 1:
        condition = False
    div += 1

print(maxi)