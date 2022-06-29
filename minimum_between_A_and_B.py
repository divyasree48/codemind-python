n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
if a>b:
    a,b=b,a
l=[]
for i in range(a,b+1):
    if i in arr:
        l.append(i)
if(len(l)>0):
    print(min(l))
else:
    print(-1)