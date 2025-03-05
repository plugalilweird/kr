def gcd(a, b):
    while b != 0:
         a, b = b, a%b
    return a

a = int(input())
b = int(input())



gcd_result=gcd(a, b)

lcm = (a * b)//gcd_result
print(lcm)
