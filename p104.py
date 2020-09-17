def pandigital(n):
    return sorted(str(n)) == list('123456789')


def find_last():
    n = 2
    val1 = 1
    val2 = 1
    while True:
        val1, val2 = val2, val1 + val2
        val2 %= 10 ** 9
        n += 1
        if pandigital(val2):
            yield n


def truncate_top(n1, n2):
    return (n1 // 10 ** 20, n2 // 10 ** 20)


def top_pandigital(n):
    top = str(n)[:9]
    return sorted(top) == list('123456789')


def find_top():
    n = 2
    val1 = 1
    val2 = 1
    while True:
        val1, val2 = val2, val1 + val2
        if val2 >= 10 ** 40:
            val1, val2 = truncate_top(val1, val2)
        n += 1
        if top_pandigital(val2):
            yield n


def solve():
    get_last = find_last()
    get_top = find_top()
    last, top = next(get_last), next(get_top)
    while True:
        if last == top:
            return last
        elif last > top:
            top = next(get_top)
        else:
            last = next(get_last)
