#Binary Search. Given an array, sort it and search an item. Return Found or Not Found
def binary_search(my_arr, my_item):
    start = 0
    end = len(my_arr)
    while start < end:
        mid = (start + end)// 2
        if my_arr[mid] is my_item:
           return "Found"
           break
        elif my_arr[mid] > my_item:
           end = mid
        else:
           start = mid+1
    return "Not Found"

my_arr = [80, 10, 11, 15, 8, 9, 31,3 ]
my_item = 15
my_arr.sort()

print(binary_search(my_arr, my_item))
