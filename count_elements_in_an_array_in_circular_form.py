n=int(input())
l=list(map(int,input().split()))
k=l[0]
b=l[1]
l.append(k)
l.append(b)
c=0
for i in range(1,len(l)-1):
    if abs((l[i-1]%2)-(l[i+1]%2))==1:
        c+=1
print(c)