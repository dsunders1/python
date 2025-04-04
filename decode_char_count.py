#Decode a string. Each letter of the string followed by number of times each letter appeared
word = "hello"
counts = {}
for char in word:
  if char not in counts:
     counts[char] = 1
  else:
     counts[char] = counts[char] + 1

decode_str = ""
for char in counts:
  decode_str = decode_str + char + str(counts[char])

print(decode_str)
