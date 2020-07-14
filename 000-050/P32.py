"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
def is_pandigital(p1, p2, product):
    """
    p1, p2 numbers. multiplicand and multiplier. p1 is 2 digits and p2 3 digits.
    product = p1 * p2 (4 digits)
    returns true if digits 1-9 are included in p1, p2 and their product.
    """
    str_p1 = str(p1)
    str_p2 = str(p2)
    str_product = str(product)
    if len(str_product) != 4:
        return False
    # Digit 0 isn't present
    str_all = str_p1 + str_p2 + str_product
    if '0' in str_all: 
        return False
    #Verify that the string of all digits has nine possible digits
    str_set = set(str_all)
    if len(str_set) != 9:
        return False
    return True

def is_pandigitalb(p1, p2, product):
    """
    p1, p2 numbers. multiplicand and multiplier. p1 is 1 digits and p2 4 digits.
    product = p1 * p2 (4 digits)
    returns true if digits 1-9 are included in p1, p2 and their product.
    """
    str_p1 = str(p1)
    str_p2 = str(p2)
    str_product = str(product)
    if len(str_product) != 4:
        return False
    # Digit 0 isn't present
    str_all = str_p1 + str_p2 + str_product
    if '0' in str_all: 
        return False
    #Verify that the string of all digits has nine possible digits
    str_set = set(str_all)
    if len(str_set) != 9:
        return False
    return True
    
pandigital_products = []
# p1 2 digits and p2 3 digits
for p1 in range(10,100):
    for p2 in range(100,1000):
        product = p1*p2
        if is_pandigital(p1, p2, product):
            pandigital_products.append(product)

# p1 1 digit and p2 4 digits
for p1 in range(1,10):
    for p2 in range(1000,10000):
        product = p1*p2
        if is_pandigitalb(p1, p2, product):
            pandigital_products.append(product)

print(sum(set(pandigital_products)))
