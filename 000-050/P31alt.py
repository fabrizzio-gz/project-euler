def sum_coins(coins):
    """
    coins is a list of the number of coins of 1P, 50p, 20p, 10p, 5p, 2p and 1p. A list of len() = 7
    Returns the sum of coins
    """
    values = [100, 50, 20, 10, 5, 2, 1]
    total = 0
    for index in range(len(coins)):
        total += coins[index] * values[index]
    return total

counter = 1 # When using 2P only

for P1 in range(3):
    range50 = (200 - P1*100)//50
    for p50 in range(range50 + 1):
        range20 = (200 - P1*100 - p50*50)//20
        for p20 in range(range20 + 1):
            range10 = (200 - P1*100 - p50*50 - p20*20)//10
            for p10 in range(range10 + 1):
                range5 = (200 - P1*100 - p50*50 - p20*20 - p10*10)//5
                for p5 in range(range5 + 1):
                    range2 = (200 - P1*100 - p50*50 - p20*20 - p10*10 - p5*5)//2
                    for p2 in range(range2 + 1):
                        range1 = 200 - P1*100 - p50*50 - p20*20 - p10*10 - p5*5 - p2*2
                        for p1 in range(range1 + 1):
                            coins = [P1, p50, p20, p10, p5, p2, p1]
                            if sum_coins(coins) == 200:
                                counter +=1

print(counter)