#For a miltiline string create a list
#Create a dictionary from the list with unique key and value as count
#sort the dictionary and print key and value

userInput = '''smoketest-xap_xpc_integration runs smoketest on AMBER N
smoketest-n-1-on-amber-n also runs on AMBER N
Both of these have passed.  Muthu, you can go ahead and update the UI team accordingly.'''

dict1 = {}
for i in userInput.split('\n'):
   for j in i.split():
       if j not in dict1:
          dict1[j] = 1
       else:
          dict1[j] += 1      

for key in sorted(dict1):
    print(key + " = " + str(dict1[key]))
