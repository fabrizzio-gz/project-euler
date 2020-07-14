"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" 
when writing out numbers is in compliance with British usage.
"""
numbers = dict()

numbers[0] = '' # For evaluation purposes, to add nothing
numbers[1] = 'one'
numbers[2] = 'two'
numbers[3] = 'three'
numbers[4] = 'four'
numbers[5] = 'five'
numbers[6] = 'six'
numbers[7] = 'seven'
numbers[8] = 'eight'
numbers[9] = 'nine'
numbers[10] = 'ten'
numbers[11] = 'eleven'
numbers[12] = 'twelve'
numbers[13] = 'thirteen'
numbers[14] = 'fourteen'
numbers[15] = 'fifteen'
numbers[16] = 'sixteen'
numbers[17] = 'seventeen'
numbers[18] = 'eighteen'
numbers[19] = 'nineteen'
numbers[20] = 'twenty'
numbers[30] = 'thirty'
numbers[40] = 'forty'
numbers[50] = 'fifty'
numbers[60] = 'sixty'
numbers[70] = 'seventy'
numbers[80] = 'eighty'
numbers[90] = 'ninety'
# don't forget to add 'hundred' and 'and' to >=100

max_num = 1000
char_count = 0

for n in range(1, max_num + 1):
    if n <= 20:
        char_count += len(numbers[n])
    elif n < 100:
        tens = n // 10
        tens *= 10
        units = n % 10
        char_count += len(numbers[tens]) + len(numbers[units])
    elif n < 1000:
        num = n
        hundreds = num // 100
        num = num % 100
        tens = num // 10
        tens *= 10
        units = num % 10
        if n % 100 != 0:
            if num <= 20:
                # Special treatment for numbers 1 - 20
                char_count += len (numbers[hundreds]) + len('hundred') + len('and') + len(numbers[num])
            else:
                char_count += len (numbers[hundreds]) + len('hundred') + len('and') + len(numbers[tens]) + len(numbers[units])
        else:
            char_count += len (numbers[hundreds]) + len('hundred') # No 'and' present
    else:
        char_count += len('one') + len('thousand')

print(char_count)