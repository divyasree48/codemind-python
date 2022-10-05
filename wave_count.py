n=int(input())
l=list(map(int,input().split()))
#print(l)
if n%2==0:
    a=(n-1)//2
else:
    a=n//2
c=0
for i in range(1,len(l)-1,2):
    if (l[i-1]<l[i] and l[i+1]<l[i]):
        c+=1
if c!=a:
    print(-1)
else:
    print(c)