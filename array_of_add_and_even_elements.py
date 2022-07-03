n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    if arr[i]%2!=0:
        l.append(arr[i])
for i in range(len(arr)):
    if arr[i]%2==0:
        l.append(arr[i])
print(*l)