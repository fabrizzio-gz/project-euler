from math import factorial
from itertools import combinations
from p103 import get_groups, verify


def main():
    with open("p105_sets.txt") as file:
        raw_data = file.read().splitlines()

    total_sum = 0

    for set_ in raw_data:
        set_ = list(map(int, set_.split(',')))
        if verify(set_):
            total_sum += sum(set_)

    print(total_sum)


if __name__ == main():
    main()
