"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated
 numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
 being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.
"""
import prime as prime_mod

# Valid only for numbers of 6 digits with varying [1st_digit]xxxx[last_digit]

def produce_variations(pos_x, last_digits, prime_list):
    """
    pos_x: list of "x"s positions
    last_digits: list of possible last digits
    prime_list: A list of possible integer values
    Returns a dictionary. key: identifier *xx**[last_digit] -> value: count of possible iterations 
    that are in prime_list
    """
    digit1 = '123456789'
    digit_x = '1234567890'
    values_dict = {}
    for positionx_tuple in pos_x:
        # Allocate the possible indexes to 'x's and to variable digits (other1 and other2)
        index_x1, index_x2, index_x3, index_x4 = positionx_tuple
        # Iterator for first digit
        for digit1_val in digit1:
            if digit1_val == '5':
                print('Halfway iteration 1st digit')
            for digit_final in last_digits:
                # Creating the key for dictionary
                key = ['0', '0', '0', '0', '0', '0']
                key[0] = digit1_val
                key[index_x1] = 'x'
                key[index_x2] = 'x'
                key[index_x3] = 'x'
                key[index_x4] = 'x'
                key[5] = digit_final
                key_val = ''.join(key)
                # List containing the iterations relative to the key
                values_dict[key_val] = 0
                for digitx in digit_x:
                    # creating the value:
                    value = ['0', '0', '0', '0', '0', '0']
                    value[0] = digit1_val
                    value[index_x1] = digitx
                    value[index_x2] = digitx
                    value[index_x3] = digitx
                    value[index_x4] = digitx
                    value[5] = digit_final
                    value_val = int(''.join(value))
                    if value_val in prime_list:
                        values_dict[key_val] += 1
    return values_dict


prime_list = prime_mod.list_primes(1000000, 99999)
print('here1')
last_digits = '1379'
pos_x = [(1, 2, 3, 4)]
print('here2')
variations_dict = produce_variations(pos_x, last_digits, prime_list)
print('here3')
max_count = 0
max_key = 'x'
print(variations_dict)
for key in variations_dict:
    if variations_dict[key] > max_count:
        max_count = variations_dict[key]
        max_key = key
print(max_key, max_count)
