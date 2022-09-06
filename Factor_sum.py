def fac(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c
l=list(map(int,input().split(',')))
k=0
a=[]
for i in l:
    s=fac(i)
    if s in l:
        k+=1
        a.append(i)
b=sorted(a)
if k==0:
    print(-1)
else:
    print(*b)