n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=d=0
for i in a:
    c+=i
for i in b:
    d+=i
if c>d:
    print(0)
else:
    print(d-c)