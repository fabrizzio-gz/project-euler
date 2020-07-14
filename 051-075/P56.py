max_digits = 0
for a in range(90,100):
    for b in range (90,100):
        sum_digits = sum(map(int, list(str(a**b))))
        if sum_digits > max_digits:
            max_digits = sum_digits
print(max_digits)