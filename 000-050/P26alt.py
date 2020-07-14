"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions 
with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 
has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal 
fraction part.
"""
from decimal import Decimal, getcontext

def getMaxCycle(str_num):
    """
    str_num: any sequence of chars
    Returns the length of the longest sequence of repeating chars
    """
    # Break into parts and check equality
    # Assume minimal recurring cycle of length 3
    chars = set(list(str_num[:-2]))
    # Check it's not only one number repeating
    if len(chars) == 1:
        return 1
    n = len(str_num)
    len_cycle = n//2
    len_check = 1
    repeats = []
    while len_check <= len_cycle:
        str_sub = str_num[:len_check+1]
        index = str_num.find(str_sub, len_check+1)
        if index == len_check+1:
            repeats.append(str_sub)
        len_check += 1
    # Check there are no repetitions:
    if len(repeats) > 1:
        unit = repeats[0]
        if repeats[1] == 2*unit:
            # There's repetition
            return len(unit)
        else:
            return max(map(len, repeats))
    elif len(repeats) == 1:
        return len(repeats[0])
    else:
        return 0

precision = 100
getcontext().prec = precision
start = 990
finish = 999
max_cycles = {}
for quot in range(start,finish + 1):
    num = 1 / Decimal(quot)
    str_num = str(num)
    # Delete '0.'
    str_num = str_num[2:]
    str_copy = str_num[:]
    # Delete 0 in advance
    for char in str_copy:
        if char == '0':
            str_num = str_num[1:]
        else:
            break
    max_len = 0
    # To verify the number has infinite digits
    if len(str_num) == precision:
        for index in range(len(str_num)//2):
            len_cycle = getMaxCycle(str_num[index:])
            if len_cycle > max_len:
                max_len = len_cycle
    if max_len != 0:
        #print('Cycle of {} for number {}'.format(max_len, num))
        max_cycles[max_len] = quot
    #else:
        #print('No repetition for number {}'.format(num))

max_len = max(max_cycles.keys())
print('The greatest quotient is for {}, with a cycle of {} digits.'.\
format(max_cycles[max_len], max_len))
print(1/Decimal(993))