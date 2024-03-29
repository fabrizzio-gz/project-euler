"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the 
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
 abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can
 be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown 
 that all integers greater than 28123 can be written as the sum of two abundant numbers. However, 
 this upper limit cannot be reduced any further by analysis even though it is known that the 
 greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant 
numbers.
"""
import pickle

def divisors(number):
    divisors = [1]
    if number % 2 == 0:
        step = 1
    else:
        step = 2
    for divisor in range(1, number//2, step):
        if divisor not in divisors:
            if divisor != 1:
                if number % divisor == 0:
                    divisors.append(divisor)    
                    if divisor != 1 and divisor != number//divisor:
                        divisors.append(number//divisor)
    return divisors

def sum_divisors(number):
    return sum(divisors(number))

abundant_numbers = []
for number in range(12, 28123):
    if sum_divisors(number) > number:
        abundant_numbers.append(number)

with open('abundant_nums.pkl', 'wb') as f:
    pickle.dump(abundant_numbers, f)

print('Done')

