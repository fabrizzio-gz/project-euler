def best_dir(col_index, row_index, pyr):
    # Decides to go down (left) or to go right
    down = pyr[row_index + 1][col_index]
    right = pyr[row_index + 1][col_index + 1]
    if down > right:
        # Stays on same column
        return col_index
    # Moves one column to the right
    return col_index + 1

triangle_matrix = []
with open('p067_triangle.txt') as triangle:
    for line in triangle:
        triangle_matrix.append(list(map(int, line.split())))
pyr = triangle_matrix

for row_index in range(len(pyr) - 2, -1, -1):
    # Current row
    row = pyr[row_index]
    next_row = pyr[row_index + 1]
    for col_index in range(len(row)):
        best_index = best_dir(col_index, row_index, pyr)
        row[col_index] += next_row[best_index]

print('The sum of the values is', pyr[0][0])