from decimal import Decimal, getcontext
import math

def getReverseString(number):
    """
    number is any quotient
    Returns the inversed string of the quotient, not taking the last digit nor the initial '0.'
    """
    number_str = str(number)
    # Reverse string, not taking last digit (can be rounded) nor first ones '0.'
    number_str = number_str[-2:2:-1]
    return number_str

def getCycles(string):
    """
    numbe_revstr is any sequence of chars (digits in this case)
    Iterates over chars and returns the repeating cycle, if any
    """
    # Verify it's not a 1 digit sequence by checking first 10 elements
    if len(set(string[0:11])) == 1:
        return 1
    cycle_max = len(string)//2 
    cycles = []
    # Get cycles as strings
    for cycle_len in range(1, cycle_max):
        str1 = string[0:cycle_len+1]
        str2 = string[cycle_len+1:2*cycle_len+2]
        # Avoid repetition of cycles
        if str1 == str2:
            if len(cycles) >= 1:
                unit_cycle = cycles[0]
                # Verify is not repetition
                str1.replace(unit_cycle, '')
                if not str1:
                    cycles.append(str2)
            else:
                cycles.append(str1)
    # Replace the first cycle in all cycles to avoid 
    if cycles:
        return cycles[0]
    else:
        return 0


precision = 10000
getcontext().prec = precision
max_cycle = 0
max_denominator = 0
for denominator in range(2,1000):
    number = 1 / Decimal(denominator)
    # Get rid of first 0
    number *= 10**int(math.log10(denominator))
    # Verify it's a cycling number
    if len(str(number)) >= 100: 
        number_revstr = getReverseString(number)
        cycle = getCycles(number_revstr)
        cycle_len = len(str(cycle))
        if cycle_len > max_cycle:
            max_cycle = cycle_len
            max_denominator = denominator
print(max_denominator,max_cycle)



