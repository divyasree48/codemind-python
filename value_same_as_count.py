n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    if arr.count(arr[i])==arr[i]:
        if arr[i] not in l:
            l.append(arr[i])
print(len(l))