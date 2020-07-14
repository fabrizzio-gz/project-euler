from decimal import Decimal, getcontext
import math

def getDec (quotient):
    """
    quotient: Decimal number
    return: length of cycling decimals
    """
    decimals = 10 * quotient
    # Get decimals numbers first
    while (decimals - quotient) % 1 != 0:
        print((decimals - quotient) % 1)
        decimals *= 10
    digits = str(int(decimals - quotient))
    # Get only decimals after digits
    decimals %= 1
    decimals *= 10**len(digits)
    quotient_str = str(int(decimals))
    deplace = 0
    finished = False
    for deplace in range(len(digits)):
        for index1 in range(len(digits) - deplace):
            if digits[index1 + deplace] != quotient_str[index1]:
                break
            if index1 + deplace == len(digits) - 1:
                finished = True
        if finished:
            break
    digits = digits[deplace:]
    return len(digits)

precision = 20
getcontext().prec = precision
dict_lens = {}
for denominator in range(6,7):
    quotient = 1/Decimal(denominator)
    if len(str(quotient)) >= precision:
        # Getting rid of first 0s
        mult = 10**(int(math.log10(denominator)))
        quotient *= mult
        print('Len {} for quotient {}'.format(str(getDec(quotient)), str(denominator)))
        dict_lens[quotient] = getDec(quotient)

max_quotient = max(dict_lens.values())
print(max_quotient)

