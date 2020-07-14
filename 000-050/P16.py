num = 2 ** 1000
num_str = str(num)
sum_digits = 0
for digit in num_str:
    sum_digits += int(digit)

print(sum_digits)
print(num)
