count1 = 0
# L is even
for L in range(12, 10**2, 2):#int(1.5*10**6)):
    up_b = round((1 - 2**.5/2)*L)
    count_tri = 0
    b = 0
    for a in range(2, up_b + 1):
        t = (L-a)
        c = (a**2 + t**2) / (2*t)
        if a != b and abs(c - int(c)) < .0001:
            count_tri += 1
            b = L - round(c) - a
            if count_tri > 1:
                break
    if count_tri == 1:
        count1 += 1 
print(count1)