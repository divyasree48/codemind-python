n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
if a>b:
    a,b=b,a
l=[]
for i in range(len(arr)):
    for j in range(a,b+1):
        if(arr[i]==j):
            l.append(j)
if(len(l)>0):
    print(*l)
else:
    print(-1)