"""

A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def is_palindrome(n):
    ntext = str(n)
    right = -1
    for i in range(len(ntext)//2):
        if ntext[i] != ntext[right]:
            return False
        right -= 1
    return True

def is_3dig(n):
    initial = int(n**.5)
    for div in range(initial, 500, -1):
        if n % div == 0:
            factor1 = div
            factor2 = n/div
            if factor2 < 1000:
                print("Got the factors:", factor1, factor2)
                return True
    return False


n = 999**2
condition = True

while condition:
    if is_palindrome(n):
        print("Found palindrome", n,"...analyzing.")
        if is_3dig(n):
            print("Yes!")
            condition = False
        else:
            print("Nope!")
            n -= 1
    else:
        n -= 1

print(n)