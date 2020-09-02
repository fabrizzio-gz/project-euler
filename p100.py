##
# Problem 100
##

# Finding arrangement with more than 10**12 balls with 50%
# probability of getting a red ball.

def get_prob(total, red):
    return (red * (red - 1), total * (total - 1))


#breakpoint()
total = 20
while True:
    #print(total)
    red = int(20 * 
    num, denom = get_prob(total, red)
    
    if 2*num == denom:
        print(total, red)
    else:
        if 2*num > denom:
            f = lambda x: x - 1
            cond = lambda num, denom: 2*num > denom
        else:
            f = lambda x: x + 1
            cond = lambda num, denom: 2*num < denom
        red = f(red)

        while cond(num, denom):
            num, denom = get_prob(total, red)
            if num * 2 == denom:
                print(total, red)
            red = f(red)

    total += 1
