##
# Problem 99
##

# Getting line of largest number of base ** exponent list.
# Idea: Get number of digits with log10
from math import log10


bases = []
exps = []
with open('p099_base_exp.txt') as file:
    line = file.readline()
    while line:
        line = line.split(',')
        bases.append(int(line[0]))
        exps.append(int(line[1]))
        line = file.readline()

max_v = 0
for index in range(len(bases)):
    test = exps[index] * log10(bases[index])
    if test > max_v:
        max_v = test
        line = index + 1
print(line)
