def gcd(first, second):
    if first < second:
       first, second = second, first
    gcd = 1
    if first % second == 0:
        return second
    
    for num in range(second, 0, -1):
        if first % num == 0 and second % num == 0:
            gcd = num
            break
    return gcd

print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 12 & 4 =", gcd(12, 4))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(336, 360))
