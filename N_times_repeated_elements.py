n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=set(l)
a=[]
for i in s:
    if l.count(i)==k:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    for i in a:
        print(i,end=' ')