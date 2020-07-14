"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below

"""
r1 = [75]
r2 = [95, 64]
r3 = [17, 47, 82]
r4 = [18, 35, 87, 10]
r5 = [20, 4, 82, 47, 65]
r6 = [19, 1, 23, 75, 3, 34]
r7 = [88, 2, 77, 73, 7, 63, 67]
r8 = [99, 65, 4, 28, 6, 16, 70, 92]
r9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
r10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
r11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
r12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
r13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
r14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
r15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

pyr = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]

# Test values
p1 = [0]
p2 = [2, 0]
p3 = [0, 1, 0]
p4 = [0, 0, 0, 0]
p5 = [0, 1, 0, 0, 3]

pyr = [p1, p2, p3, p4, p5]




def get_dir(col_index, row_index, pyr):
    # Get sum of elements below current column below current row
    opt_down = 0
    opt_right = 0
    right_col_add = 1
    for row_i, row in enumerate(pyr):
        # Start sum below current row
        # print('Current row last item is', str(row[-1]))
        if row_i > row_index:
            down_col += row[col_index]
            # Add the right elements in diagonal starting from current col_index
            right_col += row[col_index + right_col_add]
            right_col_add += 1
    if down_col < right_col:
        # Go one step to the right, else keep going down
        return col_index + 1
    return col_index

current_col = 0
max_sum = 0
for current_row, row in enumerate(pyr):
    max_sum += row[current_col]
    next_col = get_dir(current_col, current_row, pyr)
    current_col = next_col

print('The sum of the values is', max_sum)