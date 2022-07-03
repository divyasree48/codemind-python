n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
d=0
for i in range(len(arr)):
    if arr[i]<a or arr[i]>b:
        d+=arr[i]
print(d)
        