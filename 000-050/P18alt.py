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

def best_dir(col_index, row_index, pyr):
    # Decides to go down (left) or to go right
    down = pyr[row_index + 1][col_index]
    right = pyr[row_index + 1][col_index + 1]
    if down > right:
        # Stays on same column
        return col_index
    # Moves one column to the right
    return col_index + 1

for row_index in range(len(pyr) - 2, -1, -1):
    # Current row
    row = pyr[row_index]
    next_row = pyr[row_index + 1]
    for col_index in range(len(row)):
        best_index = best_dir(col_index, row_index, pyr)
        row[col_index] += next_row[best_index]


print('The sum of the values is', pyr[0][0])