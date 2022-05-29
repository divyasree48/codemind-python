arr=list(map(int,input().split()))
arr=sorted(arr)
n=len(arr)
print((arr[n-1]-1)*(arr[n-2]-1))
