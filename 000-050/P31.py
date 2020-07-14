"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins 
in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
def sum_coins(coins):
    """
    coins is a list of the number of coins of 1p,2p,5p,10p,20p,50p,1P and 2 P. A list of len() = 8
    Returns the sum of coins
    """
    values = [1, 2, 5, 10, 20, 50, 100, 200]
    total = 0
    for index in range(len(coins)):
        total += coins[index] * values[index]
    return total

counter = 0
for p1 in range(201):
    for p2 in range(101):
        for p5 in range(41):
            for p10 in range(21):
                for p20 in range(11):
                    for p50 in range(5):
                        for P1 in range(3):
                            for P2 in range(2):
                                coins = [p1, p2, p5, p10, p20, p50, P1, P2]
                                if sum_coins(coins) == 200:
                                    counter +=1

print(counter)
