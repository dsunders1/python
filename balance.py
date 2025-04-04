open = ['(', '[', '{' ]
close = [ ')', ']', '}' ]
pairs = [ '()', '[]', '{}' ]

def balan(str1):
  stack = []
  for chr in str1:
     if chr in open:
        stack.append(chr)
     elif chr in close:
        pair = stack.pop() + chr
        if pair not in pairs:
           return "NO"
  if len(stack) != 0:
     return "NO"
  return "YES"

str1 = "{{}}"
print(balan(str1))
   
