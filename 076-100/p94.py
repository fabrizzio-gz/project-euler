#!/usr/bin/python3.8

##
# Problem 94
##

# Getting the sum of the perimeters of all 'almost equilateral'
# triangles with integer perimeters and areas, with a perimeter
# less than 1 billion.

# Idea: Brute force.

import sys
from time import time
from decimal import *

def int_area(side1, side2):
    """
    Verifies if the area of a triangle of sides: side1, side1,
    side2 is integral.
    Returns True or False
    """
    h = (side1**2 - (side2/2)**2)**.5
    return h - int(h) == 0

def int_area_decimal(side1, side2):
    """
    Verification for extra precision.
    Executed only if int_area succeeds.
    """
    side1 = Decimal(side1)
    side2 = Decimal(side2)
    h = (side1**2 - (side2/2)**2).sqrt()
    return h - int(h) == 0


def area(side1, side2):
    h = (side1**2 - (side2/2)**2)**.5
    return side2 * h / 2

def main(limit):
    """
    Calculates the sum of the perimeters of integral equilateral
    triangeles, such that perimeter <= limit.
    """
    start = time()
    triangles = []
    total_perimeter = 0
    side = 3
    while True:
        side_min = side - 1
        side_max = side + 1
        if int_area(side, side_min) and int_area_decimal(side, side_min):
            triangles.append((side, side_min))
            if total_perimeter + 2*side + side_min >= limit:
                break
            else:
                total_perimeter += 2*side + side_min
                print('Perimeter: {1}, Area: {0}'.format(area(side, side_min), 2*side + side_min))
        elif int_area(side, side_max) and int_area_decimal(side, side_max):
            triangles.append((side, side_max))
            if total_perimeter + 2*side + side_max >= limit:
                break
            else:
                total_perimeter += 2*side + side_max
                print('Perimeter: {1}, Area: {0}'.format(area(side, side_max), 2*side + side_max))
        side += 2
        
    print('Elapsed: {} seconds'.format(round(time() - start, 2)))
    print(triangles)
    print(total_perimeter)


# Command line usage: $python3 p94.py <limit> 
main(int(sys.argv[1]))
# Python terminal:
# main(10**9)
