import math
n=int(input())
a=(n*(n+1))//2
b=a*a
c=(n*(n+1)*((2*n)+1))//6
if c>b:
    print(c-b)
else:
    print(b-c)