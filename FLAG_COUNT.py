n=int(input())
a=b=2
c=0
l=[]
for i in range(n):
    l.append(a)
    c=a+b
    a=b
    b=c
print(l[n-1])