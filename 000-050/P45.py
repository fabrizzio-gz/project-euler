"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
t = [n*(n+1)//2 for n in range(1,100001)]
p = [n*(3*n-1)//2 for n in range(1,100001)]
h = [n*(2*n-1) for n in range(1,100001)]

for index in range(len(t)):
    if t[index] in p and t[index] in h:
        print(index)