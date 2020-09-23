from math import factorial
from itertools import combinations


def get_groups(group, size):
    """
    Returns all groups of size `size` using `group` elements without 
    repetition of elements
    """
    lgroup = len(group)
    if len(group) < 2 * size:
        return None

    groups = []
    # Take only first half of the combinations to avoid repetition
    possible_combinations = factorial(2 * size) // (factorial(size)) ** 2 // 2
    for sub_group in combinations(group, 2*size):
        counter = 0
        group_set = []
        for group1 in combinations(sub_group, size):
            counter += 1
            group2 = set(sub_group) - set(group1)
            if counter > possible_combinations:
                break
            else:
                groups.append([list(group1), list(group2)])
    return groups


def verify(total_group):
    """Checks the required conditions are met"""
#    breakpoint()
    max_size = len(total_group)
    min_sum = max(total_group)
    total_group.sort()
    
    # Verify unique items
    if len(set(total_group)) != len(total_group):
        return False

    # Verify sub-groups
    for size in range(2, max_size//2 + 1):
        groups = get_groups(total_group, size)
        sums = []
        for group1, group2 in groups:
            sum_group1, sum_group2 = sum(group1), sum(group2)
            if sum_group1 == sum_group2:
                return False
            else:
                sums.append(sum_group1)
                sums.append(sum_group2)
        # Minimal posible sum for next bigger sized group
        min_sum = max(sums)
        sums = []

    # Verify that all sub-groups of size > max_size//2
    # have a larger sum than groups of size 
    if sum(total_group[:max_size//2 + 1]) <= min_sum:
        return False

    # Verify sub-groups of size > max_size // 2
    # Don't repeat sums
    sums = []
    for size in range(max_size // 2 + 1, max_size):
        for group in combinations(total_group, size):
            sum_group = sum(group)
            if sum_group in sums:
                return False
            else:
                sums.append(sum_group)

    return True

def special_sumset(size):
    """Returns minimized special sumsets of size elements"""
    max_possible_value = max(size * size, 2)
    min_possible_value = size
    sets = combinations(range(min_possible_value, max_possible_value), size)
    sets = list(map(list, sets))
    sets = sorted(sets, key=sum)
    for set_ in sets:
        if verify(set_):
            return set_

# special_sumset(7)
