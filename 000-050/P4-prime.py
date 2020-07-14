def is_prime(n):
    cap = int(n**.5)
    for i in range(2, cap + 1):
        if n % i == 0:
            return False
    return True

n = 1000
for i in range(1000, 1100):
    if is_prime(i):
        print(i)