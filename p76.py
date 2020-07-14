def summations(n, n_max):
    """
    Returns the possible ways to complete a block of n units
    using blocks with a maximum size n_max
    """
    count = 0
    for first_block in range(1, n_max + 1):
        if first_block == 1 and n_max == 1:  # Only one way to count
            return 1
        rest = n - first_block
        if rest == 0:  # One possible way to count
            count += 1
        elif rest > 0:  # Get all sub-set of possible counts
            count += summations(rest, first_block)
        else:  # The first block is already too big, can't continue
            break
    return count
