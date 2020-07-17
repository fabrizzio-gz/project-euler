import itertools

combinations = itertools.combinations(range(10), 1)

# Test1
count = 0
for c1 in combinations:
    for c2 in combinations:
        count += 1
print("Test1:", count)

# Test2
combinations1 = itertools.combinations(range(10), 1)
combinations2 = itertools.combinations(range(10), 1)

count = 0
for c1 in combinations1:
    for c2 in combinations2:
        count += 1
print("Test2:", count)

# Test3
combinations1 = list(itertools.combinations(range(10), 1))
combinations2 = list(itertools.combinations(range(10), 1))

count = 0
for c1 in combinations1:
    for c2 in combinations2:
        count += 1
print("Test3:", count)
