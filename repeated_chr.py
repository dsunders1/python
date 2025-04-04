#Find maximum repeated character in a string
def repeated_char(str1):
     dict1 = {}
     max_count = 0
     for chr in str1:
         if chr not in dict1:
             dict1[chr] = 1
         else:
             dict1[chr] = dict1[chr] + 1
         if dict1[chr]> max_count:
             max_count = dict1[chr]
             repeated_chr = chr
     return repeated_chr

str1 = "AAAbbbbbaaacccccccd"
print(repeated_char(str1))
