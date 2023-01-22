n,m=map(int,input().split())
l=[list(map(int,input().split()))for i in range(n)]
max=-9999
for i in l:
    c=sum(i)
    if c>max:
        max=c
for i in range(m):
    c=0
    for j in range(n):
        c+=l[j][i]
    if c>max:
        max=c
        
print(max)