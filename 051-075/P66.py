from fractions import Fraction

def get_continued_fraction(x):
    """
    Returns the next succesive fraction for sqrt(D).
    """
    def calculate_fraction(coefficients):
        """
        Produces the continued fraction corresponding to the elements in coefficients.
        Returns as Fraction type.
        """
        closest_int = coefficients[0]
        fraction_coefficients = coefficients[1:]
        sub = 0
        for coefficient in reversed(fraction_coefficients):
            sub = Fraction(1, sub + coefficient)
        return closest_int + sub

    i = int(x**.5) # Closest perfect square
    d = x - i**2 # Denominator
    a = 2*i//d # First a
    b = i - 2*i%d # First sqrt(n) - b
    num = d # First numberator when inversing fraction
    #print_fraction(x, a, b, num) # Next inverse fraction is: num / (sqrt(x) - b)
    coefficients = [i, a]
    extended_fraction = calculate_fraction(coefficients)
    yield extended_fraction
    while True:
        d = x - b**2
        # Update coefficients
        a, b, num = (b+i)*num // d, i - ((b+i)*num%d) // num, d // num
        coefficients.append(a)
        extended_fraction = calculate_fraction(coefficients)
        yield extended_fraction

squares = [x*x for x in range(1,33)]
n = 1000
D_list = [D for D in range(2, n+1) if D not in squares]
x_max = 0
D_max = 0
for D in D_list:
    solution_generator = get_continued_fraction(D)
    while True:
        solution = next(solution_generator)
        x, y = solution.numerator, solution.denominator
        if x**2 - D*y**2 == 1:
            print(f'Solution for D: {D} is: x = {x}, y = {y}')
            if x >= x_max:
                x_max = x
                D_max = D
            break
print(D_max)
# for D in D_list:
#     x = get_min(D)
#     if x >= x_max:
#         x_max = x
#     print('Checking D', D,'. Min x is:',x)


