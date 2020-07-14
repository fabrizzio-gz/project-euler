"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten 
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and 
adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly 
two-thousand common English words, how many are triangle words?
"""
def is_triangle(word):
    """
    word is a sequence of chars.
    triangle_nums is a list of triangle numbers
    Returns True if the sum of the alphabetic positions of all chars in 'words' is in triangle_nums.
    False otherwise.
    """
    global triangle_nums
    word = word.upper()
    sum_pos = 0
    for char in word:
        a_pos = ord(char) - ord('A') + 1
        sum_pos += a_pos
    if sum_pos in triangle_nums:
        return True
    return False

with open('p042_words.txt') as f:
    text = f.read()
text = text.replace('"', '') 
words = text.split(',')

triangle_nums = [n*(n+1)//2 for n in range(1,101)]

count = 0
for word in words:
    if is_triangle(word):
        count += 1
print(count)

