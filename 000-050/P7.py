""" 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(n):
    condition = True
    # Check all possible divisors from 2 to sqrt(n)
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            condition = False
            return condition
    return condition

count = 10001
counter = 0
number = 1
while counter <= count:
    if is_prime(number):
        counter +=1
    number +=1
number -= 1 # Return to last number that was prime
print(number)