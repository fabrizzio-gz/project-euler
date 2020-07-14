###
# Problem 89
##
# Getting shortest roman number writing.
# Idea: Converting roman to arabic and then getting shortest roman notation.

def arabic(roman):
    """
    roman: a string or roman characters.
    Returns the equivalent in arabic numbers (int).
    """
    global roman_dict
    # Analyze number backwards.
    roman_back = list(reversed(list(roman)))
    value = 0
    current = roman_dict[roman_back[0]]
    for char in roman_back:
        new_val = roman_dict[char]
        # Check for subtraction
        if new_val < current:
           value -= new_val
        else:
            value += new_val
        current = new_val
    return value

def shortest(arabic):
    """
    arabic: an int.
    Returns the shortest roman notation for that number.
    For values 1 - 5000
    """
    def parse(symbol, symbol5, symbol10, val):
        roman = ''
        if val == 9:
            roman += symbol + symbol10
        elif val >= 5:
            roman += symbol5 + symbol *(val - 5)
        elif val == 4:
            roman += symbol + symbol5
        else:
            roman += symbol * val
        return roman
            
    thousands = arabic // 1000
    arabic = arabic % 1000
    hundreds = arabic // 100
    arabic = arabic % 100
    tens = arabic // 10
    units = arabic % 10
    roman = ''
    roman += 'M' * thousands
    roman += parse('C', 'D', 'M', hundreds)
    roman += parse('X', 'L', 'C', tens)
    roman += parse('I', 'V', 'X', units)
    return roman
        
def get_difference(str1, str2):
    return len(str1) - len(str2)

roman_dict ={'I': 1, 'V': 5, 'X': 10,
             'L': 50, 'C': 100, 'D': 500,
             'M': 1000}

# Load file
with open('p089_roman.txt', 'r') as f:  
    roman_nums = f.read().splitlines()
diff = 0
for roman in roman_nums:
    diff += get_difference(roman, shortest(arabic(roman)))
print(diff)
