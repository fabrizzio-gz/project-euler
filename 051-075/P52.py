"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def same_digits(number1, number2):
    """
    number1, number2: an integer
    Returns True if number1 and number2 are formed by the same digits. False otherwise
    """
    number1_str = sorted(list(str(number1)))
    number2_str = sorted(list(str(number2)))
    return number1_str == number2_str
    
number = 1
current_len = 1
while True:
    numbers = [number*index for index in range(2,7)]
    conditions = map(same_digits, [number]*5, numbers)
    if all(conditions):
        print(number)
        break
    number += 1
    if number*6 > 10**current_len:
        number = current_len*10
        current_len *= 10

