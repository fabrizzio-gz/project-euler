"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and 
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the 
denominator.
"""
def get_curious(a, b, c):
    """
    a, b, c: char digits between 1 - 9
    returns list of all curious fraction combinations: a b/ a c = b/c
    """
    numerator = list(map(int, [a+b, b+a]))
    denominator = list(map(int, [a+c, c+a]))
    curious = int(b)/int(c)
    curious_list = []
    for num in numerator:
        for den in denominator:
            # Problem condition
            if num < den:
                # Check equality of floats
                if abs(num/den - curious) < 10**-4:
                    curious_list.append((num, den))
    return curious_list

digits = '123456789'
curious_list = []
for a in digits:
    for b in digits:
        for c in digits:
            curious_list += get_curious(a, b, c)
print(curious_list)