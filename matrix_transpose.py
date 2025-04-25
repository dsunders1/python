#input
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#initialize output
trans = [[0,0,0],[0,0,0],[0,0,0]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
   for j in range(cols):
       trans[j][i] = matrix[i][j]

print(trans)
