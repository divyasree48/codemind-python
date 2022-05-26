n=int(input())
arr=list(map(int,input().split()))
max=0
for i in range(len(arr)):
    c=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c>max:
        max=c
        p=arr[i]
print(p)