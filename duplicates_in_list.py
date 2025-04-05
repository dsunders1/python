my_list = [1,1,1,2,3,3,4,5]
dict1 = {}
#create a dictionary with frequency for each integer
for i in my_list:
   if i not in dict1:
      dict1[i] =1
   else:
      dict1[i] = dict1[i] + 1

#for each key in dictionary print if the value is greater than 1
for i in dict1:
  if dict1[i] > 1:
     print(i)
