from fractions import Fraction

# Maximum denominator
d = 10**6
fractions = []
closest = 428571/10**6
limit = Fraction(3, 7)
for denom in range(d, 2, -1):
    for num in range(int(.43 * denom), 1, -1):
        if num/denom >= 3/7:
            pass
        else:
            if num/denom > closest:
                print(f'Found a new closest with: {num}/{denom}')
                closest = num/denom
            break