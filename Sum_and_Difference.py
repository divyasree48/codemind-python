a,b=map(int,input().split())
c,d=map(float,input().split())
if a>b:
    e=a+b
    f=a-b
else:
    e=a+b
    f=b-a
if c>d:
    g=c+d
    h=c-d
else:
    g=c+d
    h=d-c
print(e,f)
print(g,h)