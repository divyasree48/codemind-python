n=int(input())
arr=list(map(int,input().split()))
k=int(input())
while(k):
    j=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=j
    k-=1
for i in range(0,n):
    print(arr[i],end=' ')
    
        