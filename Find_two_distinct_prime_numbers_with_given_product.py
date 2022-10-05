n=int(input())
p=[]
p.append(2)
p.append(3)
p.append(5)
for i in range(6,n+1):
    k=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            k=1
            break
    if k==0:
        p.append(i)
f=0
for i in range(len(p)):
    for j in range(len(p)):
        if i!=j:
            if p[i]*p[j]==n:
                print(p[i],p[j],end=' ')
                f=1
                break
    if f==1:
        break
if f==0:
    print(-1)
                