n=int(input())
arr=list(map(int,input().split()))
s=0
max=-9999
for i in range(n):
    s=0
    s=s+arr[i]
    for j in range(i+1,n):
        s=s+arr[j]
        if(s>max):
            max=s
for i in range(n):
    if(arr[i]>max):
        max=arr[i]
print(max)
        