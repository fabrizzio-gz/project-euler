"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def is_palindrome(string):
    """
    Returns True if string is palindrome. False Otherwise
    """
    if len(string) < 2:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return is_palindrome(string[1:-1])

def base_2(number):
    """
    Returns the number in base 2 as a string
    """
    base = 2
    if number < base:
        return str(number % base)
    else:
        return base_2(number//2) + str(number % 2)

def main():
    max_number = 10**6
    double_palindromes = []
    for number in range(1, max_number):
        if is_palindrome(str(number)):
            if is_palindrome(base_2(number)):
                double_palindromes.append(number)
    print(double_palindromes)
    print(sum(double_palindromes))

if __name__ == "__main__":
    main()
    