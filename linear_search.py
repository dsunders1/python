#Print index in the list if item is found, else return -1
def linear_search(arr, item):
  for i in range(len(arr)):
     if arr[i] == item:
        return i
  return -1
arr = [10, 5, 6,2,12,29, 8]
item = 30
index = linear_search(arr, item)
print(index)
