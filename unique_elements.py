n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    if arr.count(arr[i]):
        if arr[i] not in l:
            l.append(arr[i])
if(len(l)>0):
    print(*l)
else:
    print(-1)