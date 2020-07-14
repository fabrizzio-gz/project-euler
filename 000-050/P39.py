"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
def solutions(p, s, s2):
    """
    p: perimeter. Integer [1, 1000]
    s: list of possible sides. Integers 1-1000
    s2: list of square values. List of squares of list s.
    """
    possible_sides = []
    for a in range(1,p):
        for b in range(a, p - a):
            c2 = a**2 + b**2
            if int(c2) in s2:
                index = s2.index(c2)
                c = s[index]
            else:
                c = 0
            if a + b + c == p:
                possible_sides.append((a, b, c))
    print('Perimeter', p, 'has solutions:', possible_sides)
    return len(possible_sides)


sides = list(range(1,1001))
sides2 = [x**2 for x in sides]
max_sols = 0
max_perimeter = 0
for perimeter in range(1, 1001):
    sols = solutions(perimeter, sides, sides2)
    if sols > max_sols:
        max_sols = sols
        max_perimeter = perimeter
print(max_perimeter)