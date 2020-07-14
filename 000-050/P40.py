"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
numbers = list(range(10**7))
numbers_str_list = list(map(str, numbers))
numbers_str = ''.join(numbers_str_list)
result = int(numbers_str[10**0])*int(numbers_str[10**1])*int(numbers_str[10**2])*\
    int(numbers_str[10**3])*int(numbers_str[10**4])*int(numbers_str[10**5])*int(numbers_str[10**6])
print(result)