#Program to check if a phrase has balanced paranthesis
open = ['(', '[', '{' ]
close = [ ')', ']', '}' ]
pairs = [ '()', '[]', '{}' ]

def balanced(str1):
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

#input string
str1 = "{{}}"
print(balanced(str1))
   
