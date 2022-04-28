import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
h=s*(s-a)*(s-b)*(s-c)
ar=math.sqrt(h)
print("%.2f"%ar)