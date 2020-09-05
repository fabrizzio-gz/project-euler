# Getting sum of bad incorrect terms.
from typing import Callable
import numpy as np


def un(n: int) -> int:
    """Return nth element of sequence"""
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


def get_seq(n: int, un: Callable) -> np.array:
    """
    n : Number of elements.
    un : A function un(n)
    Return an array [un(1), un(2), ..., un(n)]
    """
    array = []
    for num in range(1, n + 1):
        array.append(un(num))
    return np.array(array)


def generate_function(coeffs: list) -> Callable[[int], int]:
    """
    coeffs : a list of coefficients a0, a1, ..., an
    for the polynomial p(x) = a0 + a1*x + ... + an*x^n
    Return a polynomial function of order len(coeffs) - 1
    """
    return lambda x: sum([coeff*x**power for power, coeff in enumerate(coeffs)])


def get_matrix(n) -> np.ndarray:
    """
    n : An int.
    Return nxn matrix to be used on system of equations:
    [(1^0 1¹ ... 1^n-1), (1 2¹ ... 2^n-1), ... (1 n ... n^n-1)]
    """
    return np.array([[x**p for p in range(n)] for x in range(1, n + 1)])


def solve_equation(A, B):
    """
    A : A nxn matrix.
    B : A n vector
    Solve Ax = B with matrix algebra
    Return x.
    """
    return np.linalg.inv(A).dot(B)


def main():
    seq = []
    dim = 11 # un is a polynomial of dimension 10
    for n in range(1, dim + 1):
        seq.append(un(n))

    # Getting the Optimum Polynomials of power n
    funcs = []
    for n in range(1, dim + 1):
        # Solving A(coeffs) = B
        coeffs = solve_equation(get_matrix(n), np.array(seq[:n]))
        funcs.append(generate_function(coeffs))

    # Last function is a corrrect OP
    funcs.pop()

    # Getting sum of BOPs, the (n+1) element for OP of dimension n
    BOP = []
    for n, fun in enumerate(funcs):
        # Since n starts from 0, add +2 to get n+1 element
        BOP.append(round(fun(n + 2)))

    print(sum(BOP))


if __name__ == "__main__":
    main()
