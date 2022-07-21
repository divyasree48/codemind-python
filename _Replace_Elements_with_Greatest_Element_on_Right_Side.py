n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if i==len(arr)-1:
        arr[i]=-1
    else:
        l=[]
        for j in range(i+1,len(arr)):
            l.append(arr[j])
            k=max(l)
        arr[i]=k
print(*arr)