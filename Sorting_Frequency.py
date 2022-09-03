n=int(input())
l1=list(map(int,input().split()))
d={}
for i in l1:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
l=[]
c=0
for i in d:
    if d[i]>1:
        c+=1
for j in range(c):
    m=ind=0
    for i in d:
        if d[i]>m:
            m=d[i]
            ind=i
    l.append(ind)
    d[ind]=0
s=[]
for i in d:
    if d[i]>0:
        s.append(i)
s.sort()
for i in s:
    l.append(i)
print(*l)