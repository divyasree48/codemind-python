n=int(input())
arr=list(map(int,input().split()))
d={}
l=[]
m=[]
ind=[]
c=0
min=999
for i in arr:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in d.keys():
    l.append(i)#num
    m.append(d[i])#frequency
f=max(m)
for i in range(len(l)):
    if(m[i]==f):
        ind.append(i)
        c+=1
for s in range(c):
    if(l[ind[s]]<min):
        min=l[ind[s]]
print(min)


    