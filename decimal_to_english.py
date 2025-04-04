#Decode decimal number from 1 to 100 in English
import sys
ones = ["", "one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","fourty","fifty","sixty","seventy", "eighty", "ninety"]

num = 68

if num in range(9):
  print(numbers[num])
  sys.exit()

if num in range(10, 19):
  one = num % 10
  print(teens[one])
  sys.exit()

if num in range(20,99):
   ten = int(num / 10)
   one = num % 10
   if one == 0:
      print(tens[ten]) 
   else:
      print(tens[ten], ones[one])
