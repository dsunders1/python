#Find repeated consecutive chars in a string
#Find which char has the longest consecutive chars
#Print the sequence

s = "abbcccddddeeeeeffffff"
longest = ''
for i in range(len(s)):
    seq = s[i]
    for j in range(i+1, len(s)):
        if s[j] == s[i]:
            seq = seq + s[j]
        else:
            break
    if len(seq) > len(longest):
        longest = seq
print(longest)
