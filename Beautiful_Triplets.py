n=int(input())
l=list(map(int,input().split()))
s=[]
s.append(n)
p=sorted(l)
k=[]
for i in p:
    if i not in k:
        k.append(i)
for i in p:
    k=l.count(i)
    for j in range(k):
        l.remove(i)
    s.append(len(l))
a=sorted(s)
b=[]
for i in range(len(a)-1,-1,-1):
    if a[i]!=0:
        if a[i] not in b:
            b.append(a[i])
            print(a[i])