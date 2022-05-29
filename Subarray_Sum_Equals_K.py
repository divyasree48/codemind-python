n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    if(arr[i]==k):
        c+=1
for i in range(n):
    s=0
    s=s+arr[i]
    for j in range(i+1,n):
        s=s+arr[j]
        if(s==k):
            c+=1
print(c)
        