#Print all least used characters in a string along with the count
str1 = "pythonprogramming"

dict1 = {}

for i in str1:
  if i not in dict1:
     dict1[i] = 1
  else:
     dict1[i] = dict1[i] + 1

lis1 = list(dict1.values())
lis1.sort()

val = lis1[0]
for key in dict1:
   if dict1[key] == val:
      print(key, str(val))
