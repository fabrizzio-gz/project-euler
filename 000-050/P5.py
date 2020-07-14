"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

topnum = 20
factors = 1

for num in range(2, topnum+1):
    # Check if current number is part of factors already
    if factors % num != 0:
        # Get highest power of number to include in factors
        print("Curent factor is", num)
        condition = True
        power = 1
        while num**power <= topnum:
            power += 1
        power -= 1 # Decrease to last power that satisfied the condition
        print("Including", num, "to the power of", power)
        factors *= num**power
    
print(factors)


