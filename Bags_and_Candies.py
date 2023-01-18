a,b,c=map(int,input().split())
d=b*c
e=a//d
f=a%d
if f==0:
    print(e)
else:
    print(e+1)