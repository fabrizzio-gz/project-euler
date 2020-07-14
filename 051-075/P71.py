from fractions import Fraction

# Maximum denominator
d = 10**6
fractions = []
closest = Fraction(3, 8)
for denom in range(2, d + 1):
    for num in range(int(.399999 * denom), int(.4 * denom)):
        if f > closest:
            closest = f
            fractions.append(f)

fractions.sort(reverse=True)
# Search for value 2/5
for index, f in enumerate(fractions):
    if f == Fraction(2, 5):
        print(fractions[index + 1].numerator)