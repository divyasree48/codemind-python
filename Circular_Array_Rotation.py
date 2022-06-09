n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
c=[]
for i in range(q):
    m=int(input())
    c.append(m)
while(k):
    j=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=j
    k-=1
for i in c:
    print(arr[i])
