#First create a list with all substrings
#Create a dictionary from the above list, with unique element from list with occurrence
#If occurence is > 1 and if the length is max return that substring
def longest_duplicate_substr(str1):
    list =[]
    n = len(str1)
    for i in range(len(str1)):
        for j in range(i + 1, n + 1):
            list.append(str1[i:j]) 
    dict1 = {}
    longest_duplicated_substring = ""
    for i in list:
        if i not in dict1:
           dict1[i] = 1
        else:
           dict1[i] += 1
           if len(i) > len(longest_duplicated_substring):
              longest_duplicated_substring = i        
    return longest_duplicated_substring

str1 = 'mississippi'
print(longest_duplicate_substr(str1))

