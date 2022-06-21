import math
n=int(input())
temp=n
rev=0
s=0
d=0
while(n):
    r=n%10
    n=n//10
    rev=rev*10+r
while(rev):
    d+=1
    r=rev%10
    rev=rev//10
    s+=pow(r,d)
if s==temp:
    print('True')
else:
    print('False')