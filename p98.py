##
# Problem 98
##

# Anagramic squares

# RACE = 9216
# C, A, R, E = 1, 2, 9, 6
# CARE = 1296
from math import sqrt
import numpy as np


def get_words(word_list: np.array, length: int) -> list:
    """
    word_list : A list of words
    length : A certan word length
    Returns a list of all words of length `length`.
    """
    len_words = np.array(list(map(len, np_words)))
    return list(np_words[len_words == length])


def is_anagram(word1: str, word2: str) -> bool:
    """Returns `True` if word1 and word2 are anagrams"""
    for char in word1:
        if word1.count(char) != word2.count(char):
            return False
    return True


def get_anagrams(words: list) -> list:
    """
    Return all words that are palindrome one another.
    """
    anagrams = []
    for i1, word in enumerate(words):
        for i2 in range(i1 + 1, len(words)):
            if sorted(word) == sorted(words[i2]):
                anagrams.append((word, words[i2]))
    return anagrams


def get_squares(l: int) -> list:
    """Returns a list of perfect squares of length `l` in reverse order """
    min_val = int(sqrt(10 ** (l - 1)))
    # Adjust for perfect_square min val
    if min_val ** 2 < 10 ** (l - 1):
        min_val += 1
    max_val = int(sqrt(10 ** l - 1))
    perfect_squares = []
    for val in range(max_val, min_val - 1, -1):
        perfect_squares.append(val ** 2)
    return perfect_squares


def get_num_anagrams(nums: list) -> list:
    """
    nums : A list of numbers
    Generates tuples (num1, num2) where num1 and num2
    are permutations one another.
    """
    for i1, n1 in enumerate(nums):
        for i2 in range(i1 + 1, len(nums)):
            if sorted(str(n1)) == sorted(str(nums[i2])):
                yield (n1, nums[i2])


def is_anagramic_square(word_tup: tuple, num_tup: tuple) -> bool:
    """Returns True if the word tuple is the same anagram as the num tuple"""
    word1, word2 = word_tup
    num1, num2 = num_tup
    num1 = str(num1)
    num2 = str(num2)

    # Check same items
    if len(set(num1)) != len(set(word1)):
        return False

#    breakpoint()
    dict1 = {}
    for index, char in enumerate(word1):
        if char not in dict1:
            dict1[char] = num1[index]
        else:
            if dict1[char] != num1[index]:
                return False

    dict2 = {}
    for index, char in enumerate(word2):
        if char not in dict2:
            dict2[char] = num1[index]
        else:
            if dict2[char] != num1[index]:
                return False

    # Find non unique keys
    values1 = dict1.values()
    values2 = dict2.values()
    if len(values1) != len(set(values1)) or \
       len(values2) != len(set(values2)):
        return False

    for index, char in enumerate(word2):
        if dict1[char] != num2[index]:
            break
    else:
        return True

    for index, char in enumerate(word1):
        if dict2[char] != num2[index]:
            return False

    return True


with open('p098_words.txt') as file:
    words = file.read().replace('"', '').split(',')

np_words = np.array(words)
finished = False
w = ('BOARD', 'BROAD')
n = (18769, 17689)
is_anagramic_square(w, n)
for l in range(4, 14 + 1):
    anagrams = get_anagrams(get_words(np_words, l))
    print('Words of length {} are:'.format(l))
    print(anagrams)
    if anagrams:
        for word_tup in anagrams:
            for num_tup in get_num_anagrams(get_squares(l)):
                if is_anagramic_square(word_tup, num_tup):
                    print(word_tup, num_tup)
                    finished = True
                    # break
#            if finished:
#                break

#    if finished:
#        break
