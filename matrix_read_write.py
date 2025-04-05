import sys
matrix = []
#length and breadth of square matrix
num = 3

print("Enter row elements of Matrix : " + str(num))
for i in range(num):
   row = []
   row_str_list = input().split()
   for i in range(len(row_str_list)):
      row.append(int(row_str_list[i]))
   matrix.append(row)
print("The matrix is")
for i in range(num):
    for j in range(num):
        print(matrix[i][j], end = " ")
    print()
