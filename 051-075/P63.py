"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, 
is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
count = 0
digit = 1
while len(str(9**digit)) == digit:
    for n in range(1, 10):
        if len(str(n**digit)) == digit:
            count += 1
    digit += 1
print(count)