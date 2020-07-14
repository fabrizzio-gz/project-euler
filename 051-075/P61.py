"""
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: 
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different 
number in the set.
"""
def create_values(fun):
    """
    fun: a function.
    Applies the function to ints and returns all of the values of 4 digits
    Returns that list as str
    """
    list_ = list(map(fun, range(1, 150)))
    list_ = [n for n in list_ if n < 10000]
    # Convert to string and add leading 0s
    list_ = list(map(str, list_))
    list_ = list(map(str.zfill, list_, [4] * len(list_)))
    return list_



def get_cycle(before, cycle, after):
    """
    before: list of numbers xxab
    cycle: list of numbers abcd
    after: list of numbers cdxx
    Returns list of target values such that abcd are in list cycle
    """
    ab = [n % 100 for n in before]
    cd = [n // 100 for n in after]
    cycle = [n for n in cycle if n // 100 in ab and n % 100 in cd]
    return cycle

def apply_cycles(vals):
    """
    vals: a list of lists of 4 digit chars
    Returns: list after applyting 'get_cycle' to each list
    """
    vals_ret = [None] * len(vals)
    for i, list_ in enumerate(vals):
        # Get last digits from current list
        last_digits = list(set([num_str[2:] for num_str in list_]))
        # Apply as filter to next list
        if i == len(vals) - 1 :
            vals_ret[0] = [num_str for num_str in vals[0] if num_str[:2] in last_digits]
        else:
            vals_ret[i + 1] = [num_str for num_str in vals[i + 1] if num_str[:2] in last_digits]
    return vals_ret
    
# Triangle numbers
tri = create_values(lambda n: n * (n + 1 ) // 2)
# Square numbers 
sqr = create_values(lambda n: n ** 2)
# Pentagonal numbers
pen = create_values(lambda n: n * (3 * n - 1 ) // 2)
# Hexagonal numbers
hex_ = create_values(lambda n: n * (2 * n - 1 ))
# Heptagonal numbers
hep = create_values(lambda n: n * (5 * n - 3 ) // 2)
# Octagonal numbers
oct_ = create_values(lambda n: n * (3 * n - 2 ))

numbers = [tri, sqr, pen, hex_, hep, oct_]

numbers = apply_cycles(numbers)

# Apply cycles until len = 1
while len(numbers[4]) > 1:
    numbers = apply_cycles(numbers)

for list_ in numbers:
    print(list_)

# for list_ in numbers:
#     print(list_)

# Get possible cycles abcd - cdef - efgh - ghij - ijkl - klab
# such that tri - sqr - pen - hex_ - hep - oct_

# # Getting front numbers
# ab1 = set(n // 100 for n in tri)
# cd1 = set(n // 100 for n in sqr)
# ef1 = set(n // 100 for n in pen)
# gh1 = set(n // 100 for n in hex_)
# ij1 = set(n // 100 for n in hep)
# kl1 = set(n // 100 for n in oct_)

# # Getting back numbers
# ab2 = set(n % 100 for n in oct_)
# cd2 = set(n % 100 for n in tri)
# ef2 = set(n % 100 for n in sqr)
# gh2 = set(n % 100 for n in pen)
# ij2 = set(n % 100 for n in hex_)
# kl2 = set(n % 100 for n in hep)

# # Filtering != 0x
# ab2 = {n for n in ab2 if n > 9}
# cd2 = {n for n in cd2 if n > 9}
# ef2 = {n for n in ef2 if n > 9}
# gh2 = {n for n in gh2 if n > 9}
# ij2 = {n for n in ij2 if n > 9}
# kl2 = {n for n in kl2 if n > 9}

# # Intersecting
# ab = ab1.intersection(ab2)
# cd = cd1.intersection(cd2)
# ef = ef1.intersection(ef2)
# gh = gh1.intersection(gh2)
# ij = ij1.intersection(ij2)
# kl = kl1.intersection(kl2)

# # Filtering with abcd
# tri = [n for n in tri  if n // 100 in ab and n % 100 in cd]
# sqr = [n for n in sqr  if n // 100 in cd and n % 100 in ef] 
# pen = [n for n in pen  if n // 100 in ef and n % 100 in gh]
# hex_= [n for n in hex_ if n // 100 in gh and n % 100 in ij]
# hep = [n for n in hep  if n // 100 in ij and n % 100 in kl]
# oct_= [n for n in oct_ if n // 100 in kl and n % 100 in ab]

# # Filtering again
# ab1 = set(n // 100 for n in tri)
# cd1 = set(n // 100 for n in sqr)
# ef1 = set(n // 100 for n in pen)
# gh1 = set(n // 100 for n in hex_)
# ij1 = set(n // 100 for n in hep)
# kl1 = set(n // 100 for n in oct_)

# ab2 = set(n % 100 for n in oct_)
# cd2 = set(n % 100 for n in tri)
# ef2 = set(n % 100 for n in sqr)
# gh2 = set(n % 100 for n in pen)
# ij2 = set(n % 100 for n in hex_)
# kl2 = set(n % 100 for n in hep)

# ab = ab1.intersection(ab2)
# cd = cd1.intersection(cd2)
# ef = ef1.intersection(ef2)
# gh = gh1.intersection(gh2)
# ij = ij1.intersection(ij2)
# kl = kl1.intersection(kl2)

# # Filtering with abcd again
# tri = [n for n in tri  if n // 100 in ab and n % 100 in cd]
# sqr = [n for n in sqr  if n // 100 in cd and n % 100 in ef] 
# pen = [n for n in pen  if n // 100 in ef and n % 100 in gh]
# hex_= [n for n in hex_ if n // 100 in gh and n % 100 in ij]
# hep = [n for n in hep  if n // 100 in ij and n % 100 in kl]
# oct_= [n for n in oct_ if n // 100 in kl and n % 100 in ab]