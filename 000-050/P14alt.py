"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

# Iterate over dictionary for the value that takes longer
max_count = 0
longest_number = 0
counts = {}
for n in range(2, 10**6 + 1):
    number = n
    count = 0
    while number != 1:
        if number in counts:
            count += counts[number]
            number = 1
        else:
            if number % 2 == 0:
                number /= 2 
            else:
                number = 3*number + 1
            count += 1
    if count > max_count:
        max_count = count
        longest_number = n
    counts[number] = count

print('The longest chain corresponds to number', longest_number, 'with a chain of:', max_count)

2**19