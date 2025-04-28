#For a given integer list, print subsets whose sum equals 7
from itertools import combinations

#function to list all subsets of integers list
def subsets(my_list):
    out = []
    for i in range(len(my_list) + 1):
        for combo in combinations(my_list, i):
            out.append(list(combo))
    return out

my_list = [6, 7, 2, 5, 1]
all_subsets = subsets(my_list)

#loop through the subsets and only print if sum=7
for i in all_subsets:
   if sum(i) == 7:
      print(i)
