"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation 
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permutations(elements, spots):
    """
    Given a set of elements. Returns a list with all the possible permutations using a given
    number of spots. 
    """
    if spots == 1:
        return elements
    else:
        permutations_list = []
        for element in elements:
            basic_elements = elements[:]
            basic_elements.remove(element)
            basic_permutations = permutations(basic_elements, spots - 1)
            # Concatenate permutation with each element
            permutations_list += [element + permutation for permutation in basic_permutations]
        return permutations_list

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
permutation = permutations(digits, 10)
permutation.sort() 
print(permutation[10**6 - 1])