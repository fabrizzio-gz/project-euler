def summations(n, n_max):
    """
    n: block of 'n' units.
    n_max: maximum block size.
    Returns the possible ways to sum block n.
    """
    count = 0
    for first_block in range(1, n_max + 1):
        if first_block == 1 and n_max == 1:
            return 1
        rest = n - first_block
        if rest == 0:  # Only one way to count
            count += 1
        elif rest > 0:  # Get all sub-set of possible counts
            count += summations(rest, first_block)
        else:  # The first block is already too big, can't continue
            break
    return count
#print(summations(100, 99))