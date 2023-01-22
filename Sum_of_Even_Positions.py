n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n,2):
    c+=l[i]
print(c)