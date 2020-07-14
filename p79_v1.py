def digits_before(x, logins):
    """
    x: any digit 0 - 9 (char)
    logins: a list of 3 digit logins
    Returns a set of all digits that come before digit "x" in logins.
    """
    before_digit_x = set()
    for login in logins:
        if x in login:
            for digit in login:
                if digit == x:
                    break
                else:
                    before_digit_x.add(digit)
    return before_digit_x

with open('p079_keylog.txt', 'r') as f:  
    logins = f.read().splitlines()
logins = list(set(logins))
#print(logins)
#print(len(logins))
first_digits = set()
second_digits = set()
third_digits = set()
for login in logins:
    first_digits.add(login[0])
    second_digits.add(login[1])
    third_digits.add(login[2])
print(first_digits, len(first_digits))
print(second_digits, len(second_digits))
print(third_digits, len(third_digits))
# Digits that appear only at the end
print(third_digits - (first_digits | second_digits))
# Digits that appear only at the beginning
print(first_digits - (second_digits | third_digits))
# Union of all digits
print(first_digits | second_digits | third_digits)
# Repeated digits 
repeated_12 = set()
repeated_13 = set()
repeated_23 = set()
repeated_123 = set()
for login in logins:
    if login[0] == login[1]:
        repeated_12.add(login[0])
    if login[0] == login[2]:
        repeated_13.add(login[0])
    if login[1] == login[2]:
        repeated_23.add(login[1])
    if login [0] == login[1] == login[2]:
        repeated_123.add(login[0])
print(repeated_12)
print(repeated_13)
print(repeated_23)
print(repeated_123)
print(first_digits - third_digits) # 3
# Get digits that come before digit 1
for digit in (first_digits | second_digits):
    print(digit, ':', digits_before(digit, logins))

