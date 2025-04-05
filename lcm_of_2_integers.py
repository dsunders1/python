def greater(x, y):
   if x > y:
     return x
   else:
     return y

def lcm(x, y):
    great = greater(x,y)
    while True:
        if (great % x == 0) and (great % y == 0):
            lcm = great
            break
        great += 1
    return lcm

print(lcm(4, 6))
print(lcm(15, 17))
