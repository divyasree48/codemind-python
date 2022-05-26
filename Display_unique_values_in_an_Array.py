n=int(input())
arr=list(map(int,input().split()))
k=0
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if(arr[i]==arr[j] and i!=j):
            c+=1
            break
    if(c==0):
        print(arr[i],end=' ')
        k+=1
if(k==0):
    print(-1)