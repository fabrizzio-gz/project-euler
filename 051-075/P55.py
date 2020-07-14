"""
f we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

For every number below ten-thousand, it will either (i) become a palindrome in less than fifty 
iterations or ii) never.
How many Lychrel numbers are there below ten-thousand?
"""
def is_palindrome(new_number):
    """
    new_number: An int
    Returns True if palindrome. Else False.
    """
    new_number_str = str(new_number)
    for index in range(len(new_number_str)//2):
        if not new_number_str[index] == new_number_str[-(index+1)]:
            return False
    return True

def is_lychrel(number):
    """
    number: An int
    Returns True if it does not become palindrome after 50 iterations. Else False.
    """
    number_str = str(number)
    for iterations in range(50):
        new_number = int(number_str) + int(number_str[::-1])
        if is_palindrome(new_number):
            return False
        number_str = str(new_number)
    return True


count = 0
for number in range(1,10000 + 1):
    if is_lychrel(number):
        count += 1
print(count)