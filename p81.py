##
# Problem 81
##
# Finding the minimum sum path in a 80 x 80 matrix.
# Idea, divide in 2 pyramids.
from copy import deepcopy

def tag_pyr(pyr):
    """
    pyr: A pyramid of numbers
    Returns a new pyramid where each item of pyr is changed to a list [number, False]
    """
    new_pyr = []
    for line in pyr:
        new_line = []
        for number in line:
            item = [number, False]
            new_line.append(item)
        new_pyr.append(new_line)
    return new_pyr

def get_minimums_for_each_path(tagged_pyr_):
    """
    tagged_pyr_: The original pyramid of values
    Returns a list with minimum sums for each path
    """
    min_sums = []
    for tag in range(len(tagged_pyr_)):
        # New copy of values
        tagged_pyr = deepcopy(tagged_pyr_)
        # Tag corresponding bottom item
        tagged_pyr[-1][tag][1] = True
        # Start from bottom, 2nd to last line, up
        for pyr_line_index in range(len(tagged_pyr) - 2, -1, -1):
            #print('Checking line:', pyr_line_index)
            for index, item in enumerate(tagged_pyr[pyr_line_index]):
                item_1 = tagged_pyr[pyr_line_index + 1][index] # Directly below
                item_2 = tagged_pyr[pyr_line_index +1][index + 1] # Below and to the right
                value_1 = item_1[0]
                value_2 = item_2[0]
                tag_1 = item_1[1]
                tag_2 = item_2[1]
                # 2 tagged values
                if tag_1 and tag_2:
                    min_val = min(value_1, value_2)
                    # Update to min sum
                    tagged_pyr[pyr_line_index][index] = [item[0] + min_val, True]
                # Only item below
                elif tag_1:
                    tagged_pyr[pyr_line_index][index] = [item[0] + value_1, True]
                # Only the other one
                elif tag_2:
                    tagged_pyr[pyr_line_index][index] = [item[0] + value_2, True]
                # Otherwise do not change
        # Add minimum sum of corresponding path
        min_sums.append(tagged_pyr[0][0][0])
    return min_sums

with open('p081_matrix.txt', 'r') as f:  
    lines_raw = f.read().splitlines()
lines = []
for line in lines_raw:
    char_line = line.split(',')
    lines.append([int(string) for string in char_line])
# Turning lines into 2 pyramids
# Pyramids
top_pyr, bot_pyr = [], []
n = 1
size = len(lines)
for level_index in range(len(lines)):
    pyr_line_top = []
    pyr_line_bot = []
    for index1 in range(n):
        i = n - index1 - 1
        j = index1
        pyr_line_top.append(lines[i][j])
        pyr_line_bot.append(lines[size - 1 - j][size - 1 - i])
        #print(n - index1, index1)
    top_pyr.append(pyr_line_top)
    bot_pyr.append(pyr_line_bot)
    n += 1
# Create tagged pyramids (to keep track of "paths"):
top_pyr_tagged = tag_pyr(top_pyr)
bot_pyr_tagged = tag_pyr(bot_pyr)

# Getting minimum path sums with indexes of diagonal value for each pyramid
# Choose one path (diagonal item) from 0 to size - 1
# Get the minimum sum using that path on each pyramid
# Sum minimums of each pyramid
# Choose min
min_sums_top = get_minimums_for_each_path(top_pyr_tagged)
min_sums_bot = get_minimums_for_each_path(bot_pyr_tagged)
min_sums_all = [min_bot + min_top for min_bot, min_top in zip(min_sums_bot, min_sums_top)]
# Eliminate duplicated bottom value
bottom_values = bot_pyr[-1]
min_sums_all = [min_sum - diagonal for min_sum, diagonal in zip(min_sums_all, bottom_values)]
print(min(min_sums_all))
