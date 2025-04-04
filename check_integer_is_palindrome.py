#Check if the given integer is a palindrome
def reverse_num(num):
   reverse = 0
   while num != 0:
      reverse = (reverse * 10) + (num % 10)
      num = num // 10
   return reverse

num = 12321
num1 = reverse_num(num)
if num == num1:
  print("Palindrome")
else:
  print("Not Palindrome")
