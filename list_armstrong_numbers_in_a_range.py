#List Armstrong Numbers between 100 and 1000
import math
lis = []
for i in range(101,999):
  i_str = str(i)
  sum = 0
  for j in i_str:
     sum = sum + pow(int(j),3)
  if sum == i:
     lis.append(i)
print(lis)
