import math

num = int(input())
n = 1
while num >= math.factorial(n):
    n = n+1
n = n-1 
while n > 1:
    a = num//math.factorial(n)
    num = num - (a*(math.factorial(n)))
    print(f'{a}*({n}!) + ', end="")
    n = n-1

a = num//math.factorial(n)
print(f'{a}*({n}!)')