#List substrings
#For each substring check if its a palindrome
#If palindrome, also check which is the longest of all palindrome substrings

def is_palindrome(s):  
    reverse = s[::-1]
    if s == reverse:
      return True
    else:
      return False  
def longest_palindrome(s):  
    n = len(s)
    longest = ""  
    for i in range(n):  
        for j in range(i+1, n+1):  
            substr = s[i:j]  
            if is_palindrome(substr) and (len(substr) > len(longest)):  
                longest = substr
    return longest
input_str = "baaac"
print(longest_palindrome(input_str))
